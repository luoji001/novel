#!/usr/bin/env bash
# 每小时把工作区改动自动提交并推送到远程当前分支（由 cron 调用）。
#
# 手工执行：
#   bash scripts/auto_commit.sh            # 真的提交 + 推送
#   bash scripts/auto_commit.sh --dry-run  # 只看会提交什么，不动仓库
#
# 运行日志：state/auto-commit.log

set -uo pipefail

REPO_DIR="/home/liang/novel-agent"
LOG_FILE="$REPO_DIR/state/auto-commit.log"
LOCK_FILE="$REPO_DIR/state/auto-commit.lock"
LOG_MAX_BYTES=$((2 * 1024 * 1024))    # 日志超过 2M 就截断，只留末尾
BLOB_MAX_BYTES=$((50 * 1024 * 1024))  # 有单个待提交文件超过 50M 就放弃本轮

# 即使 .gitignore 哪天被改坏，这些也绝不允许进提交：密钥和本地状态库
SECRET_RE='(^|/)(keys\.env$|\.env($|\.)|.*\.(pem|key|p12|pfx)$|id_(rsa|ed25519)|.*\.sqlite(-wal|-shm)?$)'

# cron 的环境极简：git 要靠 HOME 找到 ~/.gitconfig（user.name）和 ~/.git-credentials（推送凭证）
export HOME="${HOME:-/home/liang}"
export PATH="/usr/local/bin:/usr/bin:/bin"
export GIT_TERMINAL_PROMPT=0  # 凭证失效时直接失败，不要挂在那里等人输密码
unset GIT_ASKPASS SSH_ASKPASS

DRY_RUN=0
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=1

log() { printf '%s %s\n' "$(date '+%F %T')" "$*" >>"$LOG_FILE"; }

mkdir -p "$(dirname "$LOG_FILE")"

# 日志过大时只保留末尾 200 行
if [[ -f $LOG_FILE ]] && (( $(stat -c%s "$LOG_FILE") > LOG_MAX_BYTES )); then
  tail -n 200 "$LOG_FILE" >"$LOG_FILE.tmp" && mv "$LOG_FILE.tmp" "$LOG_FILE"
fi

# 上一轮没跑完就跳过本轮，避免两个进程同时动仓库
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  log "SKIP 上一轮仍在执行（锁被占用）"
  exit 0
fi

cd "$REPO_DIR" || { log "FAIL 无法进入 $REPO_DIR"; exit 1; }
git rev-parse --git-dir >/dev/null 2>&1 || { log "FAIL $REPO_DIR 不是 git 仓库"; exit 1; }

# 仓库正处于 merge/rebase/cherry-pick 等中间态时不要插手
GIT_DIR_PATH="$(git rev-parse --git-dir)"
for marker in MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD BISECT_LOG rebase-merge rebase-apply; do
  if [[ -e "$GIT_DIR_PATH/$marker" ]]; then
    log "SKIP 仓库正在进行 $marker，本轮不动"
    exit 0
  fi
done

branch="$(git symbolic-ref --quiet --short HEAD)" || {
  log "SKIP HEAD 处于游离状态（detached），本轮不动"
  exit 0
}

upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)" || upstream=""
if [[ -z $upstream ]]; then
  log "SKIP 分支 $branch 没有上游，请先手工执行：git push -u origin $branch"
  exit 0
fi
remote="${upstream%%/*}"

# ---- 先扫一遍待提交的文件，确认没有密钥、没有超大文件 ----
# 去掉 porcelain 的 3 字符状态前缀、重命名的来源侧、以及含特殊字符时的引号
candidates=()
mapfile -t candidates < <(
  git status --porcelain=v1 --untracked-files=all |
    sed -e 's/^.\{3\}//' -e 's/.* -> //' -e 's/^"\(.*\)"$/\1/'
)

for path in "${candidates[@]}"; do
  if [[ $path =~ $SECRET_RE ]]; then
    log "FAIL 待提交清单里出现敏感文件 '$path'，本轮放弃（请检查 .gitignore）"
    exit 1
  fi
  if [[ -f $path ]] && (( $(stat -c%s "$path") > BLOB_MAX_BYTES )); then
    log "FAIL 文件 '$path' 超过 ${BLOB_MAX_BYTES} 字节，本轮放弃（避免把大文件推上远程）"
    exit 1
  fi
done

if (( DRY_RUN )); then
  log "DRY-RUN $branch -> $upstream，待提交 ${#candidates[@]} 个改动"
  printf '分支：%s -> %s\n待提交改动：%d 个\n' "$branch" "$upstream" "${#candidates[@]}"
  git status --short
  printf '未推送的本地提交：%s 个\n' "$(git rev-list --count "$upstream..HEAD")"
  echo '(--dry-run：以上内容未提交、未推送)'
  exit 0
fi

# ---- 提交 ----
git add -A || { log "FAIL git add 失败"; exit 1; }

if ! git diff --cached --quiet; then
  file_count="$(git diff --cached --name-only | wc -l)"
  commit_msg="auto: $(date '+%F %T') 自动提交（$file_count 个文件）"
  if ! git commit -q -m "$commit_msg"; then
    log "FAIL git commit 失败"
    exit 1
  fi
  log "COMMIT $(git rev-parse --short HEAD) $commit_msg"
fi

# ---- 与远程对齐后推送 ----
if ! git fetch --quiet "$remote" 2>>"$LOG_FILE"; then
  log "FAIL fetch $remote 失败（网络或凭证问题），本地提交已保留，下一轮再试"
  exit 1
fi

behind="$(git rev-list --count "HEAD..$upstream")"
if (( behind > 0 )); then
  log "INFO $upstream 领先 $behind 个提交，先 rebase"
  if ! git rebase --quiet "$upstream" >>"$LOG_FILE" 2>&1; then
    git rebase --abort 2>/dev/null
    log "FAIL rebase 有冲突，已回滚到 rebase 前；请手工处理后再推送"
    exit 1
  fi
fi

ahead="$(git rev-list --count "$upstream..HEAD")"
if (( ahead == 0 )); then
  log "OK 无改动，本地与 $upstream 一致"
  exit 0
fi

if ! git push --quiet "$remote" "HEAD:refs/heads/$branch" 2>>"$LOG_FILE"; then
  log "FAIL push 失败（凭证过期或网络问题），本地提交已保留，下一轮再试"
  exit 1
fi

log "OK 已推送 $ahead 个提交到 $upstream"

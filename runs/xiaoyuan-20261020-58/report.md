# 风铃 生成报告

slug：`xiaoyuan-20261020-58`
档位：校园青春　闸门模式：observe
章数：9　总字数：19743
LLM 调用：100 次，累计 425.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蓝色笔记本的裂口 | 1667 | short | 79.4 | 0 |  | 1 |
| 2 | 磁带在抽屉里发烫 | 2537 | normal | 89.9 | 0 |  | 1 |
| 3 | 贴名签的手指 | 2093 | normal | 90.4 | 0 |  | 2 |
| 4 | 钥匙坠入尘埃 | 2197 | normal | 86.0 | 0 |  | 1 |
| 5 | 蓝色笔记本的裂口 | 2443 | normal | 90.8 | 0 |  | 2 |
| 6 | 攥紧蓝色笔记本 | 2313 | normal | 84.5 | 0 |  | 4 |
| 7 | 纸条上的字迹 | 2401 | normal | 89.7 | 0 |  | 0 |
| 8 | 攥紧蓝色笔记本 | 2374 | normal | 90.1 | 0 |  | 2 |
| 9 | 纸飞机落公告栏 | 1709 | short | 66.0 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 8.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「知道自己」×3
- 第 3 章：
  - narration_para_pct 9.8 低于目标 15.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - dialogue_chars_pct 17.0 低于目标 20.0
- 第 5 章：
  - narration_para_pct 11.6 低于目标 15.0
  - [observe] 标题重复：「蓝色笔记本的裂口」已存在
- 第 6 章：
  - 单条套路句式超限：「教务处」×21、「点了点头」×4
  - narration_para_pct 12.2 低于目标 15.0
  - [observe] 章内自我复读 18 句（如「她不知道这个名字代表什么，也不知道为什么会有这样…」）
  - [observe] 标题与《蓝色笔记本的裂口》近似 0.67 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「苏晓棠的」×4
  - [observe] 标题重复：「攥紧蓝色笔记本」已存在
- 第 9 章：
  - dialogue_chars_pct 12.5 低于目标 20.0
  - interiority_para_pct 36.0 高于目标 35.0
  - dialogue_run_mean 1.2 低于目标 1.5
  - [observe] 章内自我复读 15 句（如「她低头看着手中的排名单，数字一点点爬上视线，像一…」）

## 整书结构指标

```
chapters: 9
total_chars: 18864
chapter_chars_mean: 2096
chapter_chars_median: 2216
chapter_chars_cv: 0.14
paragraphs_mean: 40.6
dialogue_chars_pct: 20.8
dialogue_para_pct: 58.4
interiority_para_pct: 21.8
narration_para_pct: 19.8
turn_under20_pct: 87.1
turn_over200_pct: 0.0
attr_say_pct: 16.3
attr_adv_pct: 1.8
scenes_per_chapter: 1.6
dialogue_run_mean: 2.4
turn_len_median: 10
```

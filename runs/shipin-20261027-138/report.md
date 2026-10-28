# 硬币风波 生成报告

slug：`shipin-20261027-138`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6613
LLM 调用：57 次，累计 143.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙转动的瞬间 | 684 | short | 100.0 | 0 |  | 1 |
| 2 | 硬币滚落的瞬间 | 1150 | normal | 92.0 | 0 |  | 1 |
| 3 | 钥匙转动的瞬间 | 1122 | normal | 91.4 | 0 |  | 2 |
| 4 | 暂停键 | 1213 | normal | 90.6 | 0 |  | 1 |
| 5 | 证件本滑落瞬间 | 1176 | normal | 36.9 | 0 |  | 3 |
| 6 | 硬币滚落的瞬间 | 1262 | normal | 93.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「苏晓晴的」×5
- 第 2 章：
  - narration_para_pct 34.8 低于目标 35.0
- 第 3 章：
  - 单条套路句式超限：「林志远的」×3
  - [observe] 标题重复：「钥匙转动的瞬间」已存在
- 第 4 章：
  - narration_para_pct 24.0 低于目标 35.0
- 第 5 章：
  - 单条套路句式超限：「苏晓晴的」×3
  - narration_para_pct 28.1 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「今天是我第一次正式练习…」）
- 第 6 章：
  - 单条套路句式超限：「林志远的」×3
  - 情节与已写章节重复 0.81 ≥ 0.62（撞上「苏晓晴试图拿回储物格里的硬币，与教练林志远发生争执，最终…」）
  - [observe] 标题重复：「硬币滚落的瞬间」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6212
chapter_chars_mean: 1035
chapter_chars_median: 1093
chapter_chars_cv: 0.2
paragraphs_mean: 25.7
dialogue_chars_pct: 24.0
dialogue_para_pct: 62.8
interiority_para_pct: 0.0
narration_para_pct: 37.2
turn_under20_pct: 90.3
turn_over200_pct: 0.0
attr_say_pct: 21.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 2.8
turn_len_median: 10
```

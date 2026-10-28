# 黑箱 生成报告

slug：`shipin-20261027-237`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6406
LLM 调用：57 次，累计 132.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 锁扣轻响 | 540 | short | 37.8 | 0 |  | 1 |
| 2 | 钥匙串轻响 | 1000 | normal | 91.9 | 0 |  | 0 |
| 3 | 登记簿边缘的裂痕 | 1194 | normal | 93.0 | 0 |  | 1 |
| 4 | 扫帚与箱子的对峙 | 1207 | normal | 92.1 | 0 |  | 2 |
| 5 | 钥匙坠地惊寒霜 | 1087 | normal | 37.8 | 0 |  | 1 |
| 6 | 手电筒坠地 | 1372 | normal | 90.1 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 496 < 597（本章目标 1087 字的 55%）
- 第 3 章：
  - narration_para_pct 22.2 低于目标 35.0
- 第 4 章：
  - narration_para_pct 25.7 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
- 第 5 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 6011
chapter_chars_mean: 1002
chapter_chars_median: 1062
chapter_chars_cv: 0.28
paragraphs_mean: 25.3
dialogue_chars_pct: 24.5
dialogue_para_pct: 62.9
interiority_para_pct: 0.5
narration_para_pct: 36.7
turn_under20_pct: 88.1
turn_over200_pct: 0.0
attr_say_pct: 26.4
attr_adv_pct: 4.2
scenes_per_chapter: 1.2
dialogue_run_mean: 3.1
turn_len_median: 9
```

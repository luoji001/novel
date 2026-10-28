# 铜钥 生成报告

slug：`shipin-20261027-122`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6025
LLM 调用：57 次，累计 124.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板发出咔嗒声 | 765 | short | 96.9 | 0 |  | 0 |
| 2 | 摩挲铁盒边缘 | 1296 | normal | 90.7 | 0 |  | 3 |
| 3 | 铁盒侧面裂痕 | 865 | normal | 36.9 | 0 |  | 1 |
| 4 | 钥匙与登记本相遇 | 736 | normal | 22.8 | 0 |  | 1 |
| 5 | 钥匙与便签纸重合 | 1186 | normal | 89.4 | 0 |  | 0 |
| 6 | 推开锈蚀的房门 | 1171 | normal | 88.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「沈怀舟的」×3
  - narration_para_pct 15.4 低于目标 35.0
  - dialogue_run_mean 5.5 高于目标 4.0
- 第 3 章：
  - [observe] 章节过短 807 < 870（本章目标 1582 字的 55%）
- 第 4 章：
  - [observe] 章节过短 690 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5684
chapter_chars_mean: 947
chapter_chars_median: 962
chapter_chars_cv: 0.25
paragraphs_mean: 20.3
dialogue_chars_pct: 14.7
dialogue_para_pct: 46.4
interiority_para_pct: 1.8
narration_para_pct: 51.8
turn_under20_pct: 92.5
turn_over200_pct: 0.0
attr_say_pct: 21.9
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.3
turn_len_median: 8
```

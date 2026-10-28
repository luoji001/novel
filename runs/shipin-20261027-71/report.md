# 蛇皮袋 生成报告

slug：`shipin-20261027-71`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6272
LLM 调用：57 次，累计 128.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 蛇皮袋的颤动 | 632 | short | 36.5 | 0 |  | 2 |
| 2 | 身份证贴窗人影 | 1168 | normal | 92.7 | 0 |  | 0 |
| 3 | 钥匙与蛇皮袋对峙 | 1109 | normal | 93.0 | 0 |  | 0 |
| 4 | 指纹上的油渍 | 1128 | normal | 90.9 | 0 |  | 0 |
| 5 | 红布条缠手腕 | 1337 | normal | 91.4 | 0 |  | 2 |
| 6 | 铜耳环的回响 | 892 | normal | 36.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 7.7 高于目标 6.0
  - [observe] 章节过短 592 < 597（本章目标 1087 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「王翠兰的」×4
  - narration_para_pct 33.3 低于目标 35.0
- 第 6 章：
  - interiority_para_pct 6.5 高于目标 6.0
  - [observe] 章内自我复读 2 句（如「李大伟松开手，蛇皮袋缓缓落地，在瓷砖上发出轻微的…」）
  - [observe] 章节过短 816 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5861
chapter_chars_mean: 977
chapter_chars_median: 1044
chapter_chars_cv: 0.24
paragraphs_mean: 26.5
dialogue_chars_pct: 20.1
dialogue_para_pct: 47.2
interiority_para_pct: 2.4
narration_para_pct: 50.4
turn_under20_pct: 95.7
turn_over200_pct: 0.0
attr_say_pct: 47.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.2
dialogue_run_mean: 1.7
turn_len_median: 10
```

# 钥匙声 生成报告

slug：`shipin-20261027-108`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5303
LLM 调用：57 次，累计 123.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙轻响 | 366 | short | 14.8 | 0 |  | 3 |
| 2 | 钥匙坠地清响 | 686 | normal | 22.6 | 0 |  | 2 |
| 3 | 钥匙的余温 | 963 | normal | 3.1 | 0 |  | 4 |
| 4 | 钥匙与碎玻璃 | 1099 | normal | 89.5 | 0 |  | 0 |
| 5 | 拾贝记 | 1166 | normal | 55.6 | 0 |  | 2 |
| 6 | 钥匙刻痕如潮水 | 1017 | normal | 90.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 2.4 低于目标 5.0
  - narration_para_pct 91.7 高于目标 90.0
  - [observe] 章节过短 330 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 644 < 870（本章目标 1582 字的 55%）
  - [observe] 标题与《钥匙轻响》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「林小满的」×3
  - interiority_para_pct 14.3 高于目标 6.0
  - narration_para_pct 28.6 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「阳光透过百叶窗在桌面投下细密的光斑，映出三人交叠…」）
- 第 5 章：
  - interiority_para_pct 10.0 高于目标 6.0
  - narration_para_pct 30.0 低于目标 35.0

## 整书结构指标

```
chapters: 6
total_chars: 5000
chapter_chars_mean: 833
chapter_chars_median: 943
chapter_chars_cv: 0.35
paragraphs_mean: 18.2
dialogue_chars_pct: 19.9
dialogue_para_pct: 52.5
interiority_para_pct: 4.8
narration_para_pct: 42.6
turn_under20_pct: 84.6
turn_over200_pct: 0.0
attr_say_pct: 89.1
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.6
turn_len_median: 12
```

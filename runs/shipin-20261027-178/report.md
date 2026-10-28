# 红布条 生成报告

slug：`shipin-20261027-178`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5790
LLM 调用：57 次，累计 137.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙板上的细碎声响 | 520 | short | 35.7 | 0 |  | 3 |
| 2 | 钥匙上的细小刻痕 | 1154 | normal | 91.8 | 0 |  | 1 |
| 3 | 红布条系树干 | 1226 | normal | 93.3 | 0 |  | 1 |
| 4 | 钥匙与木牌对峙 | 800 | normal | 36.3 | 0 |  | 1 |
| 5 | 钥匙与疤痕的对望 | 1117 | normal | 90.9 | 0 |  | 2 |
| 6 | 红布条系树干 | 967 | normal | 88.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 1.7 低于目标 5.0
  - narration_para_pct 95.0 高于目标 90.0
  - [observe] 章节过短 463 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「林晓晴的」×4、「周德昌的」×3
- 第 3 章：
  - narration_para_pct 31.8 低于目标 35.0
- 第 4 章：
  - [observe] 章节过短 737 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 单条套路句式超限：「周德昌的」×5、「林晓晴的」×3
  - narration_para_pct 28.6 低于目标 35.0
- 第 6 章：
  - [observe] 标题重复：「红布条系树干」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5426
chapter_chars_mean: 904
chapter_chars_median: 978
chapter_chars_cv: 0.29
paragraphs_mean: 22.2
dialogue_chars_pct: 21.5
dialogue_para_pct: 55.6
interiority_para_pct: 0.7
narration_para_pct: 43.7
turn_under20_pct: 91.4
turn_over200_pct: 0.0
attr_say_pct: 66.0
attr_adv_pct: 0.0
scenes_per_chapter: 1.5
dialogue_run_mean: 1.8
turn_len_median: 10
```

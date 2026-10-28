# 蛇皮袋 生成报告

slug：`shipin-20261027-295`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6396
LLM 调用：57 次，累计 143.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙敲击蛇皮袋 | 216 | short | 15.8 | 0 |  | 3 |
| 2 | 登记簿上的指纹 | 1275 | normal | 37.7 | 0 |  | 2 |
| 3 | 竹篮砸蛇皮袋 | 1321 | normal | 94.1 | 0 |  | 1 |
| 4 | 箱子的秘密 | 923 | normal | 57.2 | 0 |  | 1 |
| 5 | 钥匙与钱包的对峙 | 1251 | normal | 38.1 | 0 |  | 4 |
| 6 | 塑料袋坠地 | 1404 | normal | 93.2 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 187 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - narration_para_pct 28.1 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「你们两个都给我冷静点…」）
- 第 3 章：
  - narration_para_pct 25.0 低于目标 35.0
- 第 4 章：
  - dialogue_chars_pct 4.6 低于目标 5.0
- 第 5 章：
  - 单条套路句式超限：「王翠兰的」×4
  - narration_para_pct 21.3 低于目标 35.0
  - dialogue_run_mean 4.1 高于目标 4.0
  - [observe] 章内自我复读 1 句（如「你是不是知道些什么？…」）

## 整书结构指标

```
chapters: 6
total_chars: 5960
chapter_chars_mean: 993
chapter_chars_median: 1168
chapter_chars_cv: 0.42
paragraphs_mean: 28.7
dialogue_chars_pct: 23.8
dialogue_para_pct: 57.9
interiority_para_pct: 1.2
narration_para_pct: 40.8
turn_under20_pct: 96.8
turn_over200_pct: 0.0
attr_say_pct: 20.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 2.7
turn_len_median: 8
```

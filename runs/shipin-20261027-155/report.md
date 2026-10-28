# 蛇皮袋 生成报告

slug：`shipin-20261027-155`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6839
LLM 调用：57 次，累计 141.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁锹撬蛇皮袋 | 974 | short | 97.5 | 0 |  | 0 |
| 2 | 布条缠绕蛇皮袋 | 1228 | normal | 90.7 | 0 |  | 0 |
| 3 | 钥匙串的节奏 | 1338 | normal | 36.5 | 0 |  | 2 |
| 4 | 硬币与门帘的轻颤 | 1143 | normal | 91.3 | 0 |  | 0 |
| 5 | 手电筒划破黑暗 | 1195 | normal | 91.2 | 0 |  | 1 |
| 6 | 铁锹撬蛇皮袋 | 955 | normal | 37.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 3 章：
  - narration_para_pct 31.0 低于目标 35.0
  - [observe] 章内自我复读 1 句（如「铁锹尖端不知何时已经靠近了她的脚边…」）
- 第 5 章：
  - 单条套路句式超限：「李建军的」×3
- 第 6 章：
  - [observe] attr_adv_pct 50.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「铁锹撬蛇皮袋」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6375
chapter_chars_mean: 1062
chapter_chars_median: 1092
chapter_chars_cv: 0.14
paragraphs_mean: 29
dialogue_chars_pct: 24.4
dialogue_para_pct: 60.0
interiority_para_pct: 1.1
narration_para_pct: 38.9
turn_under20_pct: 96.4
turn_over200_pct: 0.0
attr_say_pct: 24.5
attr_adv_pct: 10.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.4
turn_len_median: 10
```

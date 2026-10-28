# 蛇皮袋 生成报告

slug：`shipin-20261027-211`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6886
LLM 调用：57 次，累计 152.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 撕裂的蛇皮袋 | 724 | short | 92.3 | 0 |  | 1 |
| 2 | 登记簿上的直线 | 1377 | normal | 37.5 | 0 |  | 1 |
| 3 | 铁皮饭盒的豁口 | 1055 | normal | 94.1 | 0 |  | 1 |
| 4 | 钥匙与照片的对峙 | 1419 | normal | 90.0 | 0 |  | 2 |
| 5 | 铜铃撞地 | 991 | normal | 91.1 | 0 |  | 1 |
| 6 | 蛇皮袋里的身份证 | 1314 | normal | 93.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 4.0 低于目标 5.0
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「那是十年前某个秋天，他在山坡上拾荒时捡回来的…」）
- 第 3 章：
  - dialogue_chars_pct 4.6 低于目标 5.0
- 第 4 章：
  - 单条套路句式超限：「李大勇的」×3
  - attr_adv_pct 14.3 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「李大勇的」×3
- 第 6 章：
  - 单条套路句式超限：「王德发的」×3

## 整书结构指标

```
chapters: 6
total_chars: 6415
chapter_chars_mean: 1069
chapter_chars_median: 1092
chapter_chars_cv: 0.25
paragraphs_mean: 31.3
dialogue_chars_pct: 15.3
dialogue_para_pct: 44.2
interiority_para_pct: 1.1
narration_para_pct: 54.7
turn_under20_pct: 96.4
turn_over200_pct: 0.0
attr_say_pct: 33.3
attr_adv_pct: 3.5
scenes_per_chapter: 1.8
dialogue_run_mean: 1.6
turn_len_median: 8
```

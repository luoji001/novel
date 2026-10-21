# 钥匙落尘 生成报告

slug：`xiaoyuan-20261020-47`
档位：校园青春　闸门模式：observe
章数：9　总字数：19465
LLM 调用：100 次，累计 421.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙与奔跑的脚步 | 1384 | short | 96.1 | 0 |  | 1 |
| 2 | 纸条上的签名 | 1975 | normal | 93.1 | 0 |  | 1 |
| 3 | 笔记本的日期 | 2564 | normal | 91.3 | 0 |  | 2 |
| 4 | 分科表的红圈 | 2483 | normal | 90.7 | 0 |  | 1 |
| 5 | 攥钥匙等陈默 | 2412 | normal | 90.4 | 0 |  | 1 |
| 6 | 课表边缘的指纹 | 2375 | normal | 90.5 | 0 |  | 1 |
| 7 | 钥匙与沉默的光 | 2210 | normal | 90.4 | 0 |  | 1 |
| 8 | 撕页的指尖 | 2510 | normal | 90.9 | 0 |  | 2 |
| 9 | 钥匙的余温 | 1543 | short | 91.8 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.3 低于目标 20.0
- 第 2 章：
  - [observe] 章内自我复读 4 句（如「林夏低头看着手中的纸条，突然觉得这天气有些热…」）
- 第 3 章：
  - 单条套路句式超限：「知道自己」×3
  - narration_para_pct 14.8 低于目标 15.0
- 第 4 章：
  - narration_para_pct 13.7 低于目标 15.0
- 第 5 章：
  - [observe] 章内自我复读 1 句（如「林夏站在广播站门口，手里攥着那把铜钥匙…」）
- 第 6 章：
  - [observe] attr_adv_pct 50.0 > 22.0（结构塌缩）
- 第 7 章：
  - 命中套话收尾句
- 第 8 章：
  - 单条套路句式超限：「点了点头」×3
  - narration_para_pct 13.3 低于目标 15.0

## 整书结构指标

```
chapters: 9
total_chars: 18415
chapter_chars_mean: 2046
chapter_chars_median: 2244
chapter_chars_cv: 0.2
paragraphs_mean: 49.2
dialogue_chars_pct: 29.1
dialogue_para_pct: 66.9
interiority_para_pct: 14.1
narration_para_pct: 19.0
turn_under20_pct: 88.8
turn_over200_pct: 0.0
attr_say_pct: 43.3
attr_adv_pct: 8.9
scenes_per_chapter: 2.3
dialogue_run_mean: 2.9
turn_len_median: 10
```

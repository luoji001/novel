# 课表的褶皱 生成报告

slug：`xiaoyuan-20261020-53`
档位：校园青春　闸门模式：observe
章数：9　总字数：19125
LLM 调用：100 次，累计 426.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁皮盒的锁孔 | 1369 | short | 89.9 | 0 |  | 2 |
| 2 | 校服外套的褶皱 | 2214 | normal | 92.0 | 0 |  | 3 |
| 3 | 纸条上的小星星 | 2190 | normal | 86.3 | 0 |  | 2 |
| 4 | 纸条上的小星星 | 2286 | normal | 0.0 | 0 |  | 4 |
| 5 | 公告栏的纸片 | 2291 | normal | 94.3 | 0 |  | 2 |
| 6 | 钥匙串的铜环 | 2452 | normal | 89.8 | 0 |  | 2 |
| 7 | 钥匙坠入雨帘 | 2194 | normal | 86.6 | 0 |  | 2 |
| 8 | 钥匙坠入雨帘 | 2330 | normal | 89.2 | 0 |  | 3 |
| 9 | 课表的折痕 | 1790 | short | 84.5 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 14.7 低于目标 20.0
  - [observe] attr_adv_pct 100.0 > 22.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林夏点点」×3
  - narration_para_pct 13.3 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「他的位置……还有吗？…」）
- 第 3 章：
  - [observe] 章内自我复读 18 句（如「你知道我不在了吗？你知道我要转学了吗？你知道………」）
  - [observe] attr_adv_pct 23.1 > 22.0（结构塌缩）
- 第 4 章：
  - interiority_para_pct 45.5 高于目标 35.0
  - [observe] 章内自我复读 14 句（如「她知道，这个位置从此以后都将属于别人，就像那些未…」）
  - [observe] dialogue_chars_pct 6.8 < 8.0（结构塌缩）
  - [observe] 标题重复：「纸条上的小星星」已存在
- 第 5 章：
  - narration_para_pct 8.2 低于目标 15.0
  - [observe] attr_adv_pct 22.2 > 22.0（结构塌缩）
- 第 6 章：
  - 单条套路句式超限：「林夏点点」×3
  - interiority_para_pct 5.8 低于目标 8.0
- 第 7 章：
  - dialogue_chars_pct 16.7 低于目标 20.0
  - [observe] attr_adv_pct 27.3 > 22.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「林夏站在」×4
  - dialogue_chars_pct 18.8 低于目标 20.0
  - [observe] 标题重复：「钥匙坠入雨帘」已存在
- 第 9 章：
  - dialogue_chars_pct 14.4 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 18272
chapter_chars_mean: 2030
chapter_chars_median: 2109
chapter_chars_cv: 0.16
paragraphs_mean: 39.8
dialogue_chars_pct: 20.2
dialogue_para_pct: 63.2
interiority_para_pct: 18.8
narration_para_pct: 18.0
turn_under20_pct: 91.9
turn_over200_pct: 0.0
attr_say_pct: 35.0
attr_adv_pct: 15.6
scenes_per_chapter: 2.7
dialogue_run_mean: 3.3
turn_len_median: 9
```

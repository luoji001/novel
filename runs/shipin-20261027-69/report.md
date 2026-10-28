# 钥匙 生成报告

slug：`shipin-20261027-69`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6466
LLM 调用：57 次，累计 127.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙下的微光 | 811 | short | 96.0 | 0 |  | 0 |
| 2 | 杯底冰晶 | 1091 | normal | 94.0 | 0 |  | 0 |
| 3 | 信用卡撬开储物格 | 1245 | normal | 95.6 | 0 |  | 0 |
| 4 | 手机屏幕亮起 | 1377 | normal | 93.5 | 0 |  | 0 |
| 5 | 箱子上的指纹 | 1058 | normal | 94.1 | 0 |  | 0 |
| 6 | 钥匙下的微光 | 878 | normal | 37.2 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

1. 第一章和第六章均出现“钥匙下的微光”，但前者是林浩在风雪中找到车钥匙，后者是监控员发现周凯偷盗红色轿车钥匙，两者描述的“钥匙”和场景不一致，存在混淆。

2. 第二章提到林浩留下并承认车钥匙仍在车上，但第一章已描述林浩找到车钥匙，逻辑上存在矛盾。

3. 第六章提到“红色轿车钥匙”，但前文未提及“红色轿车”或“红色钥匙”，属于新增信息未提前铺垫。

## 质量债（放行但未达标的项）

- 第 6 章：
  - [observe] 章节过短 788 < 870（本章目标 1582 字的 55%）
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「钥匙下的微光」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5953
chapter_chars_mean: 992
chapter_chars_median: 984
chapter_chars_cv: 0.21
paragraphs_mean: 31.7
dialogue_chars_pct: 16.8
dialogue_para_pct: 41.6
interiority_para_pct: 1.0
narration_para_pct: 57.4
turn_under20_pct: 97.3
turn_over200_pct: 0.0
attr_say_pct: 60.0
attr_adv_pct: 13.2
scenes_per_chapter: 1.2
dialogue_run_mean: 1.6
turn_len_median: 8
```

# 分科表 生成报告

slug：`xiaoyuan-20261020-77`
档位：校园青春　闸门模式：observe
章数：9　总字数：19500
LLM 调用：100 次，累计 423.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 纸张的褶皱 | 1184 | short | 93.2 | 0 |  | 1 |
| 2 | 钥匙的重量 | 2676 | normal | 52.5 | 0 |  | 2 |
| 3 | 分科表的边缘滑动 | 2307 | normal | 90.7 | 0 |  | 1 |
| 4 | 信封与疤痕的对白 | 2521 | normal | 88.2 | 0 |  | 2 |
| 5 | 袖口的香水味 | 2460 | normal | 91.0 | 0 |  | 1 |
| 6 | 磁带的边缘摩挲 | 2233 | normal | 84.6 | 0 |  | 4 |
| 7 | 钥匙的重量 | 2581 | normal | 92.3 | 0 |  | 2 |
| 8 | 钥匙的重量 | 2106 | normal | 93.0 | 0 |  | 2 |
| 9 | 分科表的边缘滑动 | 1423 | short | 93.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 17.9 低于目标 20.0
- 第 2 章：
  - dialogue_chars_pct 14.3 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「也许有些话真的不需要说出来，但它们依然在那里，静…」）
- 第 3 章：
  - 单条套路句式超限：「苏雨桐的」×3
- 第 4 章：
  - 单条套路句式超限：「林晓阳点点」×3、「林晓阳的」×3
  - [observe] 章内自我复读 16 句（如「苏雨桐说完便转身离开，留下一句未完的话语悬在空气…」）
- 第 5 章：
  - 单条套路句式超限：「林晓阳的」×3
- 第 6 章：
  - 单条套路句式超限：「苏雨桐的」×5
  - dialogue_chars_pct 18.6 低于目标 20.0
  - narration_para_pct 12.5 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「苏雨桐笑了笑，转身看向外面，风吹动窗帘一角，露出…」）
- 第 7 章：
  - 单条套路句式超限：「苏雨桐的」×3、「他知道这」×3
  - [observe] 标题重复：「钥匙的重量」已存在
- 第 8 章：
  - 单条套路句式超限：「林晓阳和苏雨桐」×4、「苏雨桐的」×4、「他知道这」×3
  - [observe] 标题重复：「钥匙的重量」已存在
- 第 9 章：
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
  - [observe] 标题重复：「分科表的边缘滑动」已存在

## 整书结构指标

```
chapters: 9
total_chars: 18533
chapter_chars_mean: 2059
chapter_chars_median: 2207
chapter_chars_cv: 0.25
paragraphs_mean: 45.7
dialogue_chars_pct: 23.8
dialogue_para_pct: 62.0
interiority_para_pct: 12.1
narration_para_pct: 25.9
turn_under20_pct: 86.6
turn_over200_pct: 0.0
attr_say_pct: 52.1
attr_adv_pct: 3.3
scenes_per_chapter: 1.6
dialogue_run_mean: 3.1
turn_len_median: 10
```

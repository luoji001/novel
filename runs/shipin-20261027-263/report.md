# 放映机钥匙 生成报告

slug：`shipin-20261027-263`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6312
LLM 调用：57 次，累计 133.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙抵住胸膛 | 480 | short | 10.4 | 0 |  | 3 |
| 2 | 钥匙抵住胸膛 | 1209 | normal | 91.6 | 0 |  | 2 |
| 3 | 钥匙挂住纸屑 | 1248 | normal | 90.0 | 0 |  | 0 |
| 4 | 钥匙挂住纸屑 | 1060 | normal | 22.3 | 0 |  | 2 |
| 5 | 钥匙抵住胸膛 | 921 | normal | 21.2 | 0 |  | 2 |
| 6 | 钥匙摩挲金属 | 1388 | normal | 90.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 418 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「老李站在」×3
  - [observe] 标题重复：「钥匙抵住胸膛」已存在
- 第 4 章：
  - [observe] 章内自我复读 7 句（如「那是枚破损的电影票根，边缘泛黄，背面写着一行小小…」）
  - [observe] 标题重复：「钥匙挂住纸屑」已存在
- 第 5 章：
  - [observe] 章节过短 718 < 870（本章目标 1582 字的 55%）
  - [observe] 标题重复：「钥匙抵住胸膛」已存在

## 整书结构指标

```
chapters: 6
total_chars: 5598
chapter_chars_mean: 933
chapter_chars_median: 997
chapter_chars_cv: 0.35
paragraphs_mean: 42.7
dialogue_chars_pct: 14.1
dialogue_para_pct: 31.6
interiority_para_pct: 2.1
narration_para_pct: 66.3
turn_under20_pct: 98.9
turn_over200_pct: 0.0
attr_say_pct: 32.3
attr_adv_pct: 0.0
scenes_per_chapter: 1.7
dialogue_run_mean: 1.4
turn_len_median: 10
```

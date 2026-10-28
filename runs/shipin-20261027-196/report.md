# 药瓶 生成报告

slug：`shipin-20261027-196`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6753
LLM 调用：57 次，累计 146.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶与红袖章 | 618 | short | 38.1 | 0 |  | 2 |
| 2 | 挂号单撕开褶痕 | 1115 | normal | 92.8 | 0 |  | 1 |
| 3 | 登记本擦过手背 | 1252 | normal | 90.2 | 0 |  | 1 |
| 4 | 药瓶与红袖章 | 1273 | normal | 35.8 | 0 |  | 4 |
| 5 | 耳环坠入药瓶光影 | 1216 | normal | 36.2 | 0 |  | 2 |
| 6 | 登记本侧的凹槽 | 1273 | normal | 89.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「李秀兰的」×4
  - [observe] 章节过短 576 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - 单条套路句式超限：「王春梅的」×4
- 第 3 章：
  - 单条套路句式超限：「李秀兰的」×3
- 第 4 章：
  - narration_para_pct 34.4 低于目标 35.0
  - [observe] 章内自我复读 2 句（如「你女儿的名字是张小红？…」）
  - [observe] attr_adv_pct 20.0 > 18.0（结构塌缩）
  - [observe] 标题重复：「药瓶与红袖章」已存在
- 第 5 章：
  - 单条套路句式超限：「王春梅的」×3
  - [observe] 章内自我复读 2 句（如「李秀兰听见这句话，身形猛地向前冲了半步，撞得铁皮…」）
- 第 6 章：
  - 单条套路句式超限：「李秀兰的」×3

## 整书结构指标

```
chapters: 6
total_chars: 6270
chapter_chars_mean: 1045
chapter_chars_median: 1142
chapter_chars_cv: 0.23
paragraphs_mean: 31.3
dialogue_chars_pct: 17.3
dialogue_para_pct: 47.4
interiority_para_pct: 0.0
narration_para_pct: 52.6
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 45.6
attr_adv_pct: 3.8
scenes_per_chapter: 1.3
dialogue_run_mean: 1.9
turn_len_median: 8
```

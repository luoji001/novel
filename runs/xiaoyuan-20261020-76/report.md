# 雪窗 生成报告

slug：`xiaoyuan-20261020-76`
档位：校园青春　闸门模式：observe
章数：9　总字数：20832
LLM 调用：100 次，累计 435.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 名字飘落的瞬间 | 1334 | short | 98.9 | 0 |  | 0 |
| 2 | 纸张摩擦的声响 | 2583 | normal | 92.4 | 0 |  | 1 |
| 3 | 校服口袋里的硬壳 | 2183 | normal | 92.7 | 0 |  | 1 |
| 4 | 耳机线垂落的时刻 | 2710 | normal | 90.7 | 0 |  | 0 |
| 5 | 课表上的相同日期 | 2575 | normal | 92.4 | 0 |  | 3 |
| 6 | 耳机线垂落的时刻 | 2587 | normal | 90.1 | 0 |  | 4 |
| 7 | 书包带滑落的瞬间 | 2778 | normal | 89.2 | 0 |  | 3 |
| 8 | 书包带滑落的瞬间 | 2618 | normal | 90.5 | 0 |  | 4 |
| 9 | 橡皮滚落的瞬间 | 1455 | short | 92.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - narration_para_pct 14.1 低于目标 15.0
- 第 3 章：
  - narration_para_pct 13.6 低于目标 15.0
- 第 5 章：
  - narration_para_pct 9.8 低于目标 15.0
  - attr_adv_pct 21.1 高于目标 12.0
  - [observe] 章内自我复读 1 句（如「你也在准备物理补习？…」）
- 第 6 章：
  - 命中套话收尾句
  - interiority_para_pct 5.7 低于目标 8.0
  - attr_adv_pct 19.0 高于目标 12.0
  - [observe] 标题重复：「耳机线垂落的时刻」已存在
- 第 7 章：
  - dialogue_chars_pct 18.0 低于目标 20.0
  - narration_para_pct 12.1 低于目标 15.0
  - [observe] attr_adv_pct 25.0 > 22.0（结构塌缩）
- 第 8 章：
  - 单条套路句式超限：「知道自己」×3
  - narration_para_pct 10.0 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 标题重复：「书包带滑落的瞬间」已存在
- 第 9 章：
  - narration_para_pct 12.1 低于目标 15.0
  - attr_adv_pct 20.0 高于目标 12.0

## 整书结构指标

```
chapters: 9
total_chars: 19710
chapter_chars_mean: 2190
chapter_chars_median: 2437
chapter_chars_cv: 0.24
paragraphs_mean: 54
dialogue_chars_pct: 27.3
dialogue_para_pct: 70.8
interiority_para_pct: 14.9
narration_para_pct: 14.3
turn_under20_pct: 91.7
turn_over200_pct: 0.0
attr_say_pct: 37.4
attr_adv_pct: 12.7
scenes_per_chapter: 2.2
dialogue_run_mean: 3.7
turn_len_median: 8
```

# 铜钥 生成报告

slug：`xuanyi-20261019-116`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13862
LLM 调用：68 次，累计 219.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜钥匙的刻痕 | 1882 | short | 89.8 | 0 |  | 2 |
| 2 | 铁皮盒的凹凸纹路 | 3647 | normal | 89.1 | 0 |  | 4 |
| 3 | 纸页上的模糊地址 | 3249 | normal | 92.1 | 0 |  | 2 |
| 4 | 泥土中的粮袋痕迹 | 3449 | normal | 90.0 | 0 |  | 2 |
| 5 | 铜钥匙的刻痕 | 1630 | short | 92.9 | 0 |  | 4 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 19.3 低于目标 20.0
  - interiority_para_pct 24.2 高于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈怀瑾的」×13、「他知道这」×3
  - narration_para_pct 18.2 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「周婉如的声音在他身后响起，“这是一种特殊的标记，…」）
- 第 3 章：
  - 单条套路句式超限：「沈怀瑾的」×7、「沈怀瑾站在」×3、「他知道这」×3
  - narration_para_pct 13.8 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周婉如的」×6、「沈怀瑾的」×6
  - narration_para_pct 14.5 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「周婉如的」×4、「沈怀瑾的」×3
  - narration_para_pct 6.9 低于目标 20.0
  - [observe] attr_adv_pct 22.2 > 20.0（结构塌缩）
  - [observe] 标题重复：「铜钥匙的刻痕」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13238
chapter_chars_mean: 2648
chapter_chars_median: 3103
chapter_chars_cv: 0.34
paragraphs_mean: 53.2
dialogue_chars_pct: 33.6
dialogue_para_pct: 70.7
interiority_para_pct: 13.5
narration_para_pct: 15.7
turn_under20_pct: 77.2
turn_over200_pct: 0.0
attr_say_pct: 29.5
attr_adv_pct: 5.7
scenes_per_chapter: 1.6
dialogue_run_mean: 4.2
turn_len_median: 12
```

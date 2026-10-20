# 身份证 生成报告

slug：`xuanyi-20261019-150`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15342
LLM 调用：68 次，累计 227.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 回拨未接来电 | 2002 | short | 69.0 | 0 |  | 3 |
| 2 | 屏幕闪烁异常记录 | 3700 | normal | 94.5 | 0 |  | 2 |
| 3 | 屏幕闪烁异常记录 | 3886 | normal | 51.4 | 0 |  | 3 |
| 4 | 身份证背后的神秘数字 | 3834 | normal | 18.6 | 0 |  | 5 |
| 5 | 屏幕闪烁未注册用户 | 1915 | short | 90.1 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 8.5 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 章内自我复读 12 句（如「从城东到市中心大约需要四十分钟左右，但这条线路经…」）
- 第 2 章：
  - narration_para_pct 14.1 低于目标 20.0
  - [observe] attr_adv_pct 21.4 > 20.0（结构塌缩）
- 第 3 章：
  - dialogue_chars_pct 13.2 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「可那些零星的画面依旧挥之不去，在他眼前不断闪现，…」）
  - [observe] 标题重复：「屏幕闪烁异常记录」已存在
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「他知道这」×3
  - dialogue_chars_pct 8.6 低于目标 20.0
  - interiority_para_pct 20.8 高于目标 20.0
  - [observe] 章内自我复读 19 句（如「这句话他自己都不确定到底是什么意思，但他知道一件…」）
- 第 5 章：
  - narration_para_pct 18.4 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14731
chapter_chars_mean: 2946
chapter_chars_median: 3528
chapter_chars_cv: 0.33
paragraphs_mean: 52.6
dialogue_chars_pct: 23.4
dialogue_para_pct: 53.8
interiority_para_pct: 12.5
narration_para_pct: 33.7
turn_under20_pct: 77.0
turn_over200_pct: 0.0
attr_say_pct: 16.5
attr_adv_pct: 5.1
scenes_per_chapter: 2.8
dialogue_run_mean: 3.5
turn_len_median: 12
```

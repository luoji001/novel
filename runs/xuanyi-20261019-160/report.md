# 刷卡重现 生成报告

slug：`xuanyi-20261019-160`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14481
LLM 调用：68 次，累计 222.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 刷卡记录消失的瞬间 | 1998 | short | 79.0 | 0 |  | 3 |
| 2 | 屏幕上的模糊身影 | 3392 | normal | 42.9 | 0 |  | 2 |
| 3 | 报销单上的死亡时间 | 3612 | normal | 89.9 | 0 |  | 4 |
| 4 | 屏幕上的模糊身影 | 3699 | normal | 84.2 | 0 |  | 6 |
| 5 | 敲击空格键的夜晚 | 1775 | short | 74.2 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林修远的」×3
  - dialogue_chars_pct 9.8 低于目标 20.0
  - dialogue_run_mean 1.3 低于目标 1.5
- 第 2 章：
  - dialogue_chars_pct 18.1 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
- 第 3 章：
  - 单条套路句式超限：「林修远的」×7、「”沈婉清轻」×4、「沈婉清的」×4
  - narration_para_pct 4.0 低于目标 20.0
  - dialogue_run_mean 13.8 高于目标 10.0
  - [observe] attr_adv_pct 30.0 > 20.0（结构塌缩）
- 第 4 章：
  - 单条套路句式超限：「林修远的」×8、「林修远站在」×3、「为什么会」×3
  - dialogue_chars_pct 63.6 高于目标 58.0
  - narration_para_pct 3.8 低于目标 20.0
  - dialogue_run_mean 19.2 高于目标 10.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）
  - [observe] 标题重复：「屏幕上的模糊身影」已存在
- 第 5 章：
  - dialogue_chars_pct 8.3 低于目标 20.0
  - [observe] 章内自我复读 14 句（如「走到电梯口时，他回头看了一眼刚才那块显示屏，里面…」）

## 整书结构指标

```
chapters: 5
total_chars: 13790
chapter_chars_mean: 2758
chapter_chars_median: 3218
chapter_chars_cv: 0.32
paragraphs_mean: 60.4
dialogue_chars_pct: 37.3
dialogue_para_pct: 69.1
interiority_para_pct: 9.2
narration_para_pct: 21.7
turn_under20_pct: 81.4
turn_over200_pct: 0.0
attr_say_pct: 34.1
attr_adv_pct: 15.7
scenes_per_chapter: 4.4
dialogue_run_mean: 7.6
turn_len_median: 11
```

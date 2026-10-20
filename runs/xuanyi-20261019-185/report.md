# 镜中人影 生成报告

slug：`xuanyi-20261019-185`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14934
LLM 调用：68 次，累计 225.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 监控屏幕反复重播 | 1743 | short | 71.0 | 0 |  | 5 |
| 2 | 药品分类表上的名字 | 3701 | normal | 22.9 | 0 |  | 5 |
| 3 | 门锁钥匙的痕迹 | 3863 | normal | 92.2 | 0 |  | 2 |
| 4 | 收银机屏幕闪烁 | 3658 | normal | 89.4 | 0 |  | 2 |
| 5 | 纸条藏入柜缝 | 1964 | short | 92.5 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林修远的」×3
  - dialogue_chars_pct 8.5 低于目标 20.0
  - dialogue_run_mean 1.1 低于目标 1.5
  - [observe] 章内自我复读 1 句（如「林修远的心跳加快了几分…」）
- 第 2 章：
  - 单条套路句式超限：「他知道这」×4、「沈婉如的」×3、「林修远的」×3
  - dialogue_chars_pct 9.2 低于目标 20.0
  - interiority_para_pct 28.8 高于目标 20.0
  - [observe] 章内自我复读 17 句（如「他想起刚才监控画面里的那个人影，那是一个模糊的身…」）
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
- 第 3 章：
  - 单条套路句式超限：「沈婉如的」×4
  - narration_para_pct 16.7 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「沈婉如的」×5、「林修远点了点头」×3
  - narration_para_pct 16.7 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「沈婉如的」×4
  - narration_para_pct 12.2 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 14314
chapter_chars_mean: 2863
chapter_chars_median: 3511
chapter_chars_cv: 0.35
paragraphs_mean: 53.8
dialogue_chars_pct: 26.5
dialogue_para_pct: 56.6
interiority_para_pct: 16.9
narration_para_pct: 26.5
turn_under20_pct: 73.5
turn_over200_pct: 0.0
attr_say_pct: 16.3
attr_adv_pct: 10.8
scenes_per_chapter: 3.4
dialogue_run_mean: 3.4
turn_len_median: 12
```

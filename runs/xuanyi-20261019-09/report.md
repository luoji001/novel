# 蓝笔 生成报告

slug：`xuanyi-20261019-09`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14584
LLM 调用：68 次，累计 235.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药柜边缘的小点 | 2005 | short | 60.9 | 0 |  | 5 |
| 2 | 蓝色钢笔的触碰 | 3766 | normal | 93.6 | 0 |  | 2 |
| 3 | 铜牌背面的指纹 | 3266 | normal | 89.3 | 0 |  | 3 |
| 4 | 抚摸旧处方笺的褶皱 | 3646 | normal | 88.7 | 0 |  | 1 |
| 5 | 抚摸旧处方笺的褶皱 | 1896 | short | 92.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「沈文远的」×4、「他知道自己」×3
  - dialogue_chars_pct 6.9 低于目标 20.0
  - interiority_para_pct 22.0 高于目标 20.0
  - dialogue_run_mean 1 低于目标 1.5
  - [observe] 章内自我复读 16 句（如「他拿起那张纸，对着阳光照了照，又放在窗边，仔细观…」）
- 第 2 章：
  - 单条套路句式超限：「周素云的」×8、「“我不知道」×3、「沈文远的」×3
  - narration_para_pct 11.2 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「周素云的」×7
  - narration_para_pct 9.4 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 4 章：
  - narration_para_pct 14.3 低于目标 20.0
- 第 5 章：
  - narration_para_pct 14.3 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
  - [observe] 标题重复：「抚摸旧处方笺的褶皱」已存在

## 整书结构指标

```
chapters: 5
total_chars: 13892
chapter_chars_mean: 2778
chapter_chars_median: 3123
chapter_chars_cv: 0.31
paragraphs_mean: 60.8
dialogue_chars_pct: 37.1
dialogue_para_pct: 74.0
interiority_para_pct: 8.1
narration_para_pct: 17.8
turn_under20_pct: 74.0
turn_over200_pct: 0.0
attr_say_pct: 15.9
attr_adv_pct: 7.4
scenes_per_chapter: 2.2
dialogue_run_mean: 5.4
turn_len_median: 12
```

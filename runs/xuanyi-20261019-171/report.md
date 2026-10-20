# 钥匙 生成报告

slug：`xuanyi-20261019-171`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13944
LLM 调用：68 次，累计 222.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 摩挲锁痕的手指 | 1680 | short | 98.8 | 0 |  | 0 |
| 2 | 摩挲地图边缘的手指 | 3218 | normal | 92.1 | 0 |  | 6 |
| 3 | 摩挲钥匙的手指 | 3520 | normal | 89.1 | 0 |  | 5 |
| 4 | 摩挲信纸边缘的手指 | 3445 | normal | 90.8 | 0 |  | 2 |
| 5 | 摩挲铜把手的指尖 | 2076 | short | 89.6 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「沈慕云的」×6、「为什么会」×4、「周文远的」×3
  - narration_para_pct 14.6 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
  - [observe] 章内自我复读 1 句（如「副本，1930年4月…」）
  - [observe] 标题与《摩挲锁痕的手指》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 3 章：
  - 单条套路句式超限：「周文远的」×12、「沈慕云的」×9
  - narration_para_pct 9.6 低于目标 20.0
  - attr_adv_pct 18.2 高于目标 10.0
  - [observe] 章内自我复读 2 句（如「你是不是知道些什么关于那个保险柜的事情？…」）
  - [observe] 标题与《摩挲锁痕的手指》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 4 章：
  - 单条套路句式超限：「周文远的」×5、「沈慕云的」×5、「到了一个」×3
  - [observe] 标题与《摩挲地图边缘的手指》近似 0.78 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈慕云的」×5、「沈慕云站在」×3
  - narration_para_pct 8.0 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13329
chapter_chars_mean: 2666
chapter_chars_median: 3105
chapter_chars_cv: 0.31
paragraphs_mean: 53
dialogue_chars_pct: 29.7
dialogue_para_pct: 73.1
interiority_para_pct: 11.3
narration_para_pct: 15.6
turn_under20_pct: 79.7
turn_over200_pct: 0.0
attr_say_pct: 14.7
attr_adv_pct: 9.0
scenes_per_chapter: 2.4
dialogue_run_mean: 3.9
turn_len_median: 12
```

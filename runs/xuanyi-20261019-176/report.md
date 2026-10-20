# 面粉 生成报告

slug：`xuanyi-20261019-176`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：15154
LLM 调用：68 次，累计 239.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁锹移位痕迹 | 1721 | short | 97.1 | 0 |  | 3 |
| 2 | 旧钥匙攥紧的手 | 3619 | normal | 91.1 | 0 |  | 3 |
| 3 | 纸条上的数字排列 | 3531 | normal | 89.8 | 0 |  | 2 |
| 4 | 文件上的编号痕迹 | 4455 | normal | 90.5 | 0 |  | 3 |
| 5 | 面粉上的生产日期 | 1823 | short | 91.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「周素云的」×3
  - narration_para_pct 16.7 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「除非……他不想被人找到…」）
- 第 2 章：
  - 单条套路句式超限：「周素云的」×11、「陈文远的」×10、「“我不知道」×4
  - narration_para_pct 4.8 低于目标 20.0
  - [observe] 章内自我复读 2 句（如「一个叫‘防空洞’的地方…」）
- 第 3 章：
  - 单条套路句式超限：「周素云的」×7、「陈文远的」×6、「“我不知道」×3
  - narration_para_pct 17.1 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周素云的」×10、「“我不知道」×4、「点了点头“」×4
  - narration_para_pct 15.6 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
- 第 5 章：
  - 单条套路句式超限：「周素云的」×5、「为什么会」×3

## 整书结构指标

```
chapters: 5
total_chars: 14369
chapter_chars_mean: 2874
chapter_chars_median: 3375
chapter_chars_cv: 0.4
paragraphs_mean: 67.6
dialogue_chars_pct: 35.7
dialogue_para_pct: 76.3
interiority_para_pct: 9.5
narration_para_pct: 14.2
turn_under20_pct: 83.4
turn_over200_pct: 0.0
attr_say_pct: 22.4
attr_adv_pct: 7.4
scenes_per_chapter: 3.2
dialogue_run_mean: 5.5
turn_len_median: 10
```

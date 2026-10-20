# 铁钉 生成报告

slug：`xuanyi-20261019-86`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13842
LLM 调用：68 次，累计 231.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌悄然移位 | 1767 | short | 98.6 | 0 |  | 2 |
| 2 | 划痕下的密语 | 3397 | normal | 90.8 | 0 |  | 3 |
| 3 | 停摆的挂钟指针 | 3230 | normal | 89.9 | 0 |  | 2 |
| 4 | 锈钉上的刻痕密码 | 3664 | normal | 88.3 | 0 |  | 3 |
| 5 | 指针凝固在14点 | 1779 | short | 90.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「陈素云的」×5
  - [observe] attr_adv_pct 40.0 > 20.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「他知道自己」×4、「林振邦站在」×3、「为什么会」×3
  - narration_para_pct 14.1 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 10.0
- 第 3 章：
  - 单条套路句式超限：「林振邦的」×8、「陈素云的」×6、「陈素云点」×3
  - narration_para_pct 12.0 低于目标 20.0
- 第 4 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林振邦站在」×4、「林振邦的」×4、「他知道自己」×3
  - narration_para_pct 13.5 低于目标 20.0
- 第 5 章：
  - 单条套路句式超限：「林振邦的」×3
  - narration_para_pct 10.7 低于目标 20.0

## 整书结构指标

```
chapters: 5
total_chars: 13218
chapter_chars_mean: 2644
chapter_chars_median: 3064
chapter_chars_cv: 0.33
paragraphs_mean: 54.2
dialogue_chars_pct: 38.1
dialogue_para_pct: 76.7
interiority_para_pct: 9.6
narration_para_pct: 13.8
turn_under20_pct: 74.2
turn_over200_pct: 0.0
attr_say_pct: 17.3
attr_adv_pct: 11.0
scenes_per_chapter: 5.4
dialogue_run_mean: 5.5
turn_len_median: 14
```

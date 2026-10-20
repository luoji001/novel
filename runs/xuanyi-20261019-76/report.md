# 铜铃 生成报告

slug：`xuanyi-20261019-76`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：14121
LLM 调用：68 次，累计 233.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸木牌裂痕 | 1479 | short | 100.0 | 0 |  | 2 |
| 2 | 抚摸木牌裂痕 | 3942 | normal | 51.4 | 0 |  | 6 |
| 3 | 抚摸怀表铜锈 | 3747 | normal | 89.9 | 0 |  | 2 |
| 4 | 抚摸登记簿裂痕 | 3235 | normal | 91.1 | 0 |  | 4 |
| 5 | 钥匙与烟灰缸 | 1713 | short | 89.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

1. 第三章提到“王德昌从未离开”，但第四章又说“王德昌可能因发现秘密而离开”，前后矛盾。

2. 第五章提到“登记簿上竟无其名”，但第三章提到“王德昌从未真正来过”，与“登记簿上无其名”重复，缺乏逻辑递进。

3. 第二章提到“演习通知日期异常”，但未明确说明该通知与王德昌失踪之间的直接关联，导致线索断裂。

4. 第五章提到“王德昌自愿留下”，但前文多次暗示王德昌失踪或被隐瞒，人物立场无理由翻转。

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「带着一丝」×3、「沈文远的」×3
  - narration_para_pct 6.9 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「沈文远的」×3
  - dialogue_chars_pct 13.2 低于目标 20.0
  - interiority_para_pct 23.1 高于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
  - [observe] 章内自我复读 18 句（如「他曾多次提醒她不要再来这里，但李素芬始终不肯放弃…」）
  - [observe] 标题重复：「抚摸木牌裂痕」已存在
- 第 3 章：
  - 单条套路句式超限：「沈文远的」×7
  - attr_adv_pct 19.0 高于目标 10.0
- 第 4 章：
  - 单条套路句式超限：「沈文远的」×5、「“我不知道」×4
  - narration_para_pct 9.2 低于目标 20.0
  - attr_adv_pct 10.5 高于目标 10.0
  - [observe] 标题与《抚摸木牌裂痕》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「沈文远的」×3
  - narration_para_pct 16.1 低于目标 20.0
  - [observe] attr_adv_pct 25.0 > 20.0（结构塌缩）

## 整书结构指标

```
chapters: 5
total_chars: 13539
chapter_chars_mean: 2708
chapter_chars_median: 3090
chapter_chars_cv: 0.41
paragraphs_mean: 50.6
dialogue_chars_pct: 27.8
dialogue_para_pct: 68.4
interiority_para_pct: 13.6
narration_para_pct: 18.0
turn_under20_pct: 80.2
turn_over200_pct: 0.0
attr_say_pct: 21.8
attr_adv_pct: 13.6
scenes_per_chapter: 2.4
dialogue_run_mean: 4.3
turn_len_median: 10
```

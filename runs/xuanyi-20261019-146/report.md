# 车票 生成报告

slug：`xuanyi-20261019-146`
档位：悬疑推理　闸门模式：observe
章数：5　总字数：13069
LLM 调用：68 次，累计 217.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙牌的移动 | 1871 | short | 97.6 | 0 |  | 2 |
| 2 | 灯罩的暗纹 | 3203 | normal | 90.8 | 0 |  | 1 |
| 3 | 地毯上的密码 | 3149 | normal | 84.4 | 0 |  | 4 |
| 4 | 登记簿的缺失 | 3241 | normal | 90.6 | 0 |  | 3 |
| 5 | 钥匙牌的位移 | 1600 | short | 75.9 | 0 |  | 5 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 17.1 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 10.0
- 第 2 章：
  - 单条套路句式超限：「陈志远的」×5
- 第 3 章：
  - 命中套话收尾句
  - 单条套路句式超限：「周雪梅的」×3
  - dialogue_chars_pct 17.2 低于目标 20.0
  - [observe] 章内自我复读 16 句（如「周雪梅的眼神微微一闪，随即恢复平静：“那你还是先…」）
- 第 4 章：
  - 单条套路句式超限：「陈志远的」×5、「周雪梅的」×3
  - narration_para_pct 13.0 低于目标 20.0
  - attr_adv_pct 11.1 高于目标 10.0
- 第 5 章：
  - 命中套话收尾句
  - dialogue_chars_pct 11.3 低于目标 20.0
  - interiority_para_pct 24.1 高于目标 20.0
  - [observe] attr_adv_pct 33.3 > 20.0（结构塌缩）
  - [observe] 标题与《钥匙牌的移动》近似 0.83 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 5
total_chars: 12463
chapter_chars_mean: 2493
chapter_chars_median: 3011
chapter_chars_cv: 0.31
paragraphs_mean: 53.2
dialogue_chars_pct: 24.0
dialogue_para_pct: 63.6
interiority_para_pct: 13.8
narration_para_pct: 22.6
turn_under20_pct: 88.4
turn_over200_pct: 0.0
attr_say_pct: 24.7
attr_adv_pct: 10.8
scenes_per_chapter: 2.8
dialogue_run_mean: 3.9
turn_len_median: 11
```

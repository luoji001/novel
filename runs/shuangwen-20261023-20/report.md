# 旧工号牌 生成报告

slug：`shuangwen-20261023-20`
档位：爽文　闸门模式：observe
章数：10　总字数：19312
LLM 调用：97 次，累计 431.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 工号牌被压在文件下 | 1703 | normal | 99.4 | 0 |  | 2 |
| 2 | 工号牌递上桌面 | 1852 | normal | 36.8 | 0 |  | 2 |
| 3 | 旧工号牌对峙 | 1885 | normal | 92.5 | 0 |  | 1 |
| 4 | 粉笔线重新划出 | 1984 | normal | 92.9 | 0 |  | 1 |
| 5 | 锦旗悬挂 | 1770 | normal | 36.6 | 0 |  | 2 |
| 6 | 旧工号牌对峙 | 2393 | normal | 92.8 | 0 |  | 3 |
| 7 | 工号牌拍桌面 | 1713 | normal | 93.3 | 0 |  | 3 |
| 8 | 旧工号牌对峙 | 1661 | normal | 91.5 | 0 |  | 2 |
| 9 | 旧工号牌对峙 | 1705 | normal | 92.4 | 0 |  | 2 |
| 10 | 旧工号牌对峙 | 2636 | long | 37.4 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「林小满的」×5、「李国强的」×4
  - attr_adv_pct 14.3 高于目标 12.0
- 第 2 章：
  - 单条套路句式超限：「县供销社」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
- 第 3 章：
  - attr_adv_pct 21.4 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「林小满的」×4
- 第 5 章：
  - narration_para_pct 2.6 低于目标 5.0
  - [observe] attr_adv_pct 30.0 > 25.0（结构塌缩）
- 第 6 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林小满的」×5
  - [observe] 标题重复：「旧工号牌对峙」已存在
- 第 7 章：
  - 单条套路句式超限：「李国强的」×5
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 标题与《工号牌递上桌面》近似 0.77 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「李国强的」×3
  - [observe] 标题重复：「旧工号牌对峙」已存在
- 第 9 章：
  - 单条套路句式超限：「李国强的」×4、「林小满站在」×3、「县供销社」×3
  - [observe] 标题重复：「旧工号牌对峙」已存在
- 第 10 章：
  - 单条套路句式超限：「李国强的」×3、「林小满的」×3
  - [observe] attr_adv_pct 33.3 > 25.0（结构塌缩）
  - [observe] 标题重复：「旧工号牌对峙」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18327
chapter_chars_mean: 1833
chapter_chars_median: 1726
chapter_chars_cv: 0.17
paragraphs_mean: 41.6
dialogue_chars_pct: 45.1
dialogue_para_pct: 83.9
interiority_para_pct: 5.2
narration_para_pct: 10.8
turn_under20_pct: 73.2
turn_over200_pct: 0.0
attr_say_pct: 24.1
attr_adv_pct: 18.7
scenes_per_chapter: 1.5
dialogue_run_mean: 6.5
turn_len_median: 12
```

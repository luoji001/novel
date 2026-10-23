# 凭据 生成报告

slug：`shuangwen-20261022-95`
档位：爽文　闸门模式：observe
章数：10　总字数：17443
LLM 调用：97 次，累计 420.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指尖抚过符文 | 1536 | normal | 99.6 | 0 |  | 1 |
| 2 | 纸片拍案 | 1910 | normal | 92.8 | 0 |  | 0 |
| 3 | 指尖抚过符文 | 1711 | normal | 92.1 | 0 |  | 2 |
| 4 | 玉佩推文件 | 1857 | normal | 37.0 | 0 |  | 1 |
| 5 | 纸片抚过铜牌 | 1685 | normal | 93.6 | 0 |  | 1 |
| 6 | 指尖抚过凭据裂痕 | 1743 | normal | 36.3 | 0 |  | 2 |
| 7 | 指尖抚过凭据裂痕 | 1656 | normal | 93.8 | 0 |  | 2 |
| 8 | 凭据压住铜牌 | 1781 | normal | 90.8 | 0 |  | 0 |
| 9 | 指尖抚过凭据裂痕 | 1837 | normal | 92.9 | 0 |  | 2 |
| 10 | 凭据压住铜牌 | 1717 | long | 37.1 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - dialogue_run_mean 17.5 高于目标 14.0
  - [observe] 标题重复：「指尖抚过符文」已存在
- 第 4 章：
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 5 章：
  - 单条套路句式超限：「他知道自己」×3
- 第 6 章：
  - 单条套路句式超限：「验货台」×3
  - [observe] attr_adv_pct 28.6 > 25.0（结构塌缩）
- 第 7 章：
  - 命中套话收尾句
  - [observe] 标题重复：「指尖抚过凭据裂痕」已存在
- 第 9 章：
  - attr_adv_pct 12.5 高于目标 12.0
  - [observe] 标题重复：「指尖抚过凭据裂痕」已存在
- 第 10 章：
  - 单条套路句式超限：「他知道自己」×3、「验货台」×3
  - [observe] attr_adv_pct 31.2 > 25.0（结构塌缩）
  - [observe] 标题重复：「凭据压住铜牌」已存在

## 整书结构指标

```
chapters: 10
total_chars: 16534
chapter_chars_mean: 1653
chapter_chars_median: 1640
chapter_chars_cv: 0.07
paragraphs_mean: 37.7
dialogue_chars_pct: 43.0
dialogue_para_pct: 80.4
interiority_para_pct: 5.7
narration_para_pct: 13.9
turn_under20_pct: 73.0
turn_over200_pct: 0.0
attr_say_pct: 25.0
attr_adv_pct: 15.5
scenes_per_chapter: 1.6
dialogue_run_mean: 6.2
turn_len_median: 13
```

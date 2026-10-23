# 旧籍 生成报告

slug：`shuangwen-20261022-76`
档位：爽文　闸门模式：observe
章数：10　总字数：19295
LLM 调用：97 次，累计 431.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 旧籍被轻抚 | 1555 | normal | 39.9 | 0 |  | 2 |
| 2 | 旧籍被轻抚 | 1985 | normal | 91.7 | 0 |  | 3 |
| 3 | 铜钥插锁孔 | 1753 | normal | 92.4 | 0 |  | 2 |
| 4 | 旧籍被递出 | 2420 | normal | 94.5 | 0 |  | 4 |
| 5 | 签字笔被夺走 | 1831 | normal | 94.1 | 0 |  | 3 |
| 6 | 钱被推至案头 | 1953 | normal | 93.7 | 0 |  | 1 |
| 7 | 旧籍被摊开 | 1908 | normal | 94.4 | 0 |  | 3 |
| 8 | 签字笔被夺走 | 1876 | normal | 37.6 | 0 |  | 3 |
| 9 | 旧籍被摊开 | 1602 | normal | 90.8 | 0 |  | 2 |
| 10 | 旧籍被摊开 | 2402 | long | 93.7 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 0.0 低于目标 5.0
  - [observe] attr_adv_pct 30.8 > 25.0（结构塌缩）
- 第 2 章：
  - 单条套路句式超限：「林子安的」×3
  - narration_para_pct 2.6 低于目标 5.0
  - [observe] 标题重复：「旧籍被轻抚」已存在
- 第 3 章：
  - 单条套路句式超限：「李怀远的」×4
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「讲经堂」×4、「林子安站在」×3、「林子安的」×3
  - narration_para_pct 3.9 低于目标 5.0
  - dialogue_run_mean 15.3 高于目标 14.0
  - [observe] 标题与《旧籍被轻抚》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 5 章：
  - 单条套路句式超限：「讲经堂」×4、「李怀远的」×3
  - narration_para_pct 4.3 低于目标 5.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 6 章：
  - attr_adv_pct 20.0 高于目标 12.0
- 第 7 章：
  - 单条套路句式超限：「讲经堂」×5、「李怀远的」×3
  - narration_para_pct 4.8 低于目标 5.0
  - [observe] 标题与《旧籍被轻抚》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「讲经堂」×3
  - [observe] 章内自我复读 2 句（如「这些的确是从老档案里找来的，但是它们不能算作正式…」）
  - [observe] 标题重复：「签字笔被夺走」已存在
- 第 9 章：
  - 命中套话收尾句
  - [observe] 标题重复：「旧籍被摊开」已存在
- 第 10 章：
  - [observe] 标题重复：「旧籍被摊开」已存在

## 整书结构指标

```
chapters: 10
total_chars: 18271
chapter_chars_mean: 1827
chapter_chars_median: 1797
chapter_chars_cv: 0.15
paragraphs_mean: 44
dialogue_chars_pct: 50.1
dialogue_para_pct: 84.9
interiority_para_pct: 5.5
narration_para_pct: 9.6
turn_under20_pct: 70.9
turn_over200_pct: 0.0
attr_say_pct: 26.5
attr_adv_pct: 11.7
scenes_per_chapter: 1.6
dialogue_run_mean: 9.7
turn_len_median: 14
```

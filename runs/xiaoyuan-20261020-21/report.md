# 分科表 生成报告

slug：`xiaoyuan-20261020-21`
档位：校园青春　闸门模式：observe
章数：9　总字数：20527
LLM 调用：100 次，累计 434.9 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表的边缘 | 1537 | short | 98.2 | 0 |  | 1 |
| 2 | 校服外套上的汗渍 | 2615 | normal | 88.0 | 0 |  | 4 |
| 3 | 磁带塞入书包的动作 | 2457 | normal | 91.3 | 0 |  | 0 |
| 4 | 课表边缘的铅笔线 | 2292 | normal | 90.5 | 0 |  | 1 |
| 5 | 钥匙和欠条 | 2334 | normal | 93.1 | 0 |  | 1 |
| 6 | 钥匙藏进书包夹层 | 2528 | normal | 84.5 | 0 |  | 4 |
| 7 | 欠条边缘的潮湿 | 2489 | normal | 86.6 | 0 |  | 3 |
| 8 | 分科表的复印件 | 2484 | normal | 92.4 | 0 |  | 2 |
| 9 | 缴费单边缘的汗渍 | 1782 | short | 86.9 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 命中套话收尾句
- 第 2 章：
  - 单条套路句式超限：「林小满站在」×3
  - dialogue_chars_pct 15.9 低于目标 20.0
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 8 句（如「她穿着一身蓝色制服，手里拎着一叠文件，脸色看起来…」）
- 第 4 章：
  - 单条套路句式超限：「林小满的」×6
- 第 5 章：
  - narration_para_pct 12.3 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「他知道自己」×5、「”苏远低」×5
  - narration_para_pct 14.6 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 25 句（如「他知道，这把钥匙不仅仅是打开家门的工具，它更像是…」）
- 第 7 章：
  - 单条套路句式超限：「他知道这」×5
  - dialogue_chars_pct 17.3 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 8 章：
  - narration_para_pct 14.5 低于目标 15.0
  - [observe] 标题与《分科表的边缘》近似 0.62 ≥ 0.6（换个角度，别只换一个词）
- 第 9 章：
  - 单条套路句式超限：「林小满的」×3
  - dialogue_chars_pct 15.7 低于目标 20.0

## 整书结构指标

```
chapters: 9
total_chars: 19580
chapter_chars_mean: 2176
chapter_chars_median: 2344
chapter_chars_cv: 0.16
paragraphs_mean: 44.4
dialogue_chars_pct: 22.0
dialogue_para_pct: 64.2
interiority_para_pct: 17.7
narration_para_pct: 18.1
turn_under20_pct: 88.3
turn_over200_pct: 0.0
attr_say_pct: 40.7
attr_adv_pct: 8.0
scenes_per_chapter: 2.8
dialogue_run_mean: 3.2
turn_len_median: 10
```

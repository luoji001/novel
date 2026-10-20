# 铅笔印 生成报告

slug：`xiaoyuan-20261020-157`
档位：校园青春　闸门模式：observe
章数：9　总字数：20268
LLM 调用：100 次，累计 431.6 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 志愿表的褶皱一角 | 1292 | short | 97.2 | 0 |  | 1 |
| 2 | 麦克风上的指纹 | 2792 | normal | 91.2 | 0 |  | 2 |
| 3 | 校服口袋的磁带盒 | 2234 | normal | 84.2 | 0 |  | 3 |
| 4 | 手指划过公告栏 | 2646 | normal | 84.8 | 0 |  | 3 |
| 5 | 志愿表边缘的指纹 | 2266 | normal | 86.0 | 0 |  | 4 |
| 6 | 揉皱的志愿表 | 2775 | normal | 84.9 | 0 |  | 3 |
| 7 | 手指划过书包带 | 2378 | normal | 93.3 | 0 |  | 2 |
| 8 | 手指划过分科表 | 2339 | normal | 92.7 | 0 |  | 3 |
| 9 | 志愿表上的铅笔痕 | 1537 | short | 92.6 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - interiority_para_pct 5.7 低于目标 8.0
- 第 2 章：
  - 单条套路句式超限：「周子墨点了点头」×3、「周子墨的」×3
  - narration_para_pct 14.3 低于目标 15.0
- 第 3 章：
  - 单条套路句式超限：「周子墨的」×6
  - narration_para_pct 12.1 低于目标 15.0
  - [observe] 章内自我复读 32 句（如「她想起上周路过教务处的时候看到的那些文件，还有陈…」）
- 第 4 章：
  - 单条套路句式超限：「林晓棠点点」×4、「带着一丝」×4、「林晓棠点了点头」×3
  - attr_adv_pct 13.3 高于目标 12.0
  - [observe] 章内自我复读 34 句（如「陈老师看了她一眼，意味深长地说：“因为你提交的志…」）
- 第 5 章：
  - 单条套路句式超限：「林晓棠站在」×3
  - dialogue_chars_pct 18.6 低于目标 20.0
  - narration_para_pct 9.1 低于目标 15.0
  - [observe] 章内自我复读 16 句（如「然而在这个瞬间，她感受到了一股久违的动力，就像是…」）
- 第 6 章：
  - 单条套路句式超限：「林晓棠点点」×3
  - attr_adv_pct 16.7 高于目标 12.0
  - [observe] 章内自我复读 39 句（如「林晓棠看着他认真翻阅笔记本的样子，忽然觉得这个世…」）
- 第 7 章：
  - 单条套路句式超限：「周子墨的」×4、「林晓棠的」×4、「林晓棠点点」×3
  - narration_para_pct 7.7 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「林晓棠的」×3
  - narration_para_pct 10.3 低于目标 15.0
  - [observe] 与历史章节逐字重复 4 句（如「周子墨抬起头，看了她一眼，又低下头去…」）

## 整书结构指标

```
chapters: 9
total_chars: 19237
chapter_chars_mean: 2137
chapter_chars_median: 2208
chapter_chars_cv: 0.24
paragraphs_mean: 49.1
dialogue_chars_pct: 26.3
dialogue_para_pct: 67.0
interiority_para_pct: 17.2
narration_para_pct: 15.8
turn_under20_pct: 84.6
turn_over200_pct: 0.0
attr_say_pct: 33.9
attr_adv_pct: 6.2
scenes_per_chapter: 1.7
dialogue_run_mean: 3.1
turn_len_median: 10
```

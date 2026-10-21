# 药盒 生成报告

slug：`xiaoyuan-20261020-113`
档位：校园青春　闸门模式：observe
章数：9　总字数：21323
LLM 调用：100 次，累计 464.3 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 药瓶与录音笔 | 1383 | short | 95.0 | 0 |  | 2 |
| 2 | 课表消失 | 2476 | normal | 91.3 | 0 |  | 3 |
| 3 | 麦克风的颤动 | 2962 | normal | 91.5 | 0 |  | 2 |
| 4 | 校服外套的褶皱 | 2212 | normal | 88.9 | 0 |  | 3 |
| 5 | 储物柜第三格 | 2648 | normal | 90.1 | 0 |  | 3 |
| 6 | 课桌上的铁盒 | 2482 | normal | 84.8 | 0 |  | 3 |
| 7 | 成绩单的褶皱 | 2641 | normal | 89.4 | 0 |  | 1 |
| 8 | 擦拭桌面的粉笔灰 | 2451 | normal | 90.4 | 0 |  | 1 |
| 9 | 邀请函的褶皱 | 2059 | short | 90.0 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - 单条套路句式超限：「教务处」×3
  - dialogue_chars_pct 18.7 低于目标 20.0
- 第 2 章：
  - 单条套路句式超限：「林晓棠的」×4
  - interiority_para_pct 7.8 低于目标 8.0
  - attr_adv_pct 16.7 高于目标 12.0
- 第 3 章：
  - 单条套路句式超限：「林晓棠的」×6、「林晓棠点点」×3
  - attr_adv_pct 13.6 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「顾明远的」×3
  - dialogue_chars_pct 17.9 低于目标 20.0
  - narration_para_pct 13.5 低于目标 15.0
- 第 5 章：
  - 命中套话收尾句
  - 单条套路句式超限：「“我不知道」×3、「顾明远点」×3、「带着一丝」×3
  - narration_para_pct 14.6 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「林晓棠的」×4
  - dialogue_chars_pct 17.1 低于目标 20.0
  - [observe] 章内自我复读 13 句（如「周文清点头，“你知道吗，有些人其实很想靠近别人，…」）
- 第 7 章：
  - 单条套路句式超限：「顾明远点」×4
- 第 8 章：
  - 单条套路句式超限：「点了点头」×3
- 第 9 章：
  - 单条套路句式超限：「顾明远的」×7、「林晓棠点点」×3
  - narration_para_pct 10.2 低于目标 15.0
  - [observe] 章内自我复读 20 句（如「林晓棠点点头，睫毛在眼下投出细碎的阴影，“我爸爸…」）

## 整书结构指标

```
chapters: 9
total_chars: 20315
chapter_chars_mean: 2257
chapter_chars_median: 2362
chapter_chars_cv: 0.19
paragraphs_mean: 48.4
dialogue_chars_pct: 24.5
dialogue_para_pct: 66.4
interiority_para_pct: 14.0
narration_para_pct: 19.7
turn_under20_pct: 88.3
turn_over200_pct: 0.0
attr_say_pct: 42.0
attr_adv_pct: 5.6
scenes_per_chapter: 1.9
dialogue_run_mean: 3.3
turn_len_median: 9
```

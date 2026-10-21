# 分科表 生成报告

slug：`xiaoyuan-20261020-74`
档位：校园青春　闸门模式：observe
章数：9　总字数：21110
LLM 调用：100 次，累计 447.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 松动的第三颗纽扣 | 1260 | short | 91.4 | 0 |  | 1 |
| 2 | 粉笔灰染指缝 | 3187 | normal | 50.8 | 0 |  | 2 |
| 3 | 分科表上的名字 | 2100 | normal | 91.9 | 0 |  | 2 |
| 4 | 耳机里的沙沙声 | 2523 | normal | 91.7 | 0 |  | 2 |
| 5 | 摩挲校服纽扣 | 2824 | normal | 91.9 | 0 |  | 1 |
| 6 | 摩挲磁带封皮 | 2507 | normal | 31.7 | 0 |  | 3 |
| 7 | 摩挲分科表边缘 | 2574 | normal | 91.7 | 0 |  | 1 |
| 8 | 摩挲校服袖口褶皱 | 2550 | normal | 91.4 | 0 |  | 0 |
| 9 | 摩挲玻璃雾气 | 1576 | short | 92.4 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章内自我复读 17 句（如「她低头看向自己微驼的背，仿佛能看到那些藏不住的尺…」）
- 第 2 章：
  - 单条套路句式超限：「林晓棠的」×4
  - dialogue_chars_pct 14.1 低于目标 20.0
- 第 3 章：
  - 单条套路句式超限：「林晓棠的」×5、「知道自己」×4、「带着一丝」×3
  - attr_adv_pct 16.7 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「林晓棠的」×4
  - [observe] 章内自我复读 8 句（如「我记得以前有一首很像样的歌曲，现在好像找不见了…」）
- 第 5 章：
  - 单条套路句式超限：「林晓棠的」×3
- 第 6 章：
  - 单条套路句式超限：「周子航的」×3、「林晓棠的」×3
  - dialogue_chars_pct 11.8 低于目标 20.0
  - [observe] attr_adv_pct 33.3 > 22.0（结构塌缩）
- 第 7 章：
  - 单条套路句式超限：「知道自己」×4、「林晓棠站在」×3
- 第 9 章：
  - 单条套路句式超限：「林晓棠站在」×4

## 整书结构指标

```
chapters: 9
total_chars: 20230
chapter_chars_mean: 2248
chapter_chars_median: 2425
chapter_chars_cv: 0.26
paragraphs_mean: 41
dialogue_chars_pct: 20.6
dialogue_para_pct: 61.7
interiority_para_pct: 16.4
narration_para_pct: 21.8
turn_under20_pct: 89.3
turn_over200_pct: 0.0
attr_say_pct: 17.4
attr_adv_pct: 6.9
scenes_per_chapter: 2.8
dialogue_run_mean: 2.8
turn_len_median: 10
```

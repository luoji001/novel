# 信袋 生成报告

slug：`shipin-20261027-316`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6526
LLM 调用：57 次，累计 140.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 信封与红围巾 | 690 | short | 94.2 | 0 |  | 0 |
| 2 | 信封与红围巾 | 1173 | normal | 35.4 | 0 |  | 4 |
| 3 | 信封与红围巾 | 1250 | normal | 90.8 | 0 |  | 2 |
| 4 | 信封与红围巾 | 1170 | normal | 91.6 | 0 |  | 3 |
| 5 | 信封与红围巾 | 1199 | normal | 89.0 | 0 |  | 2 |
| 6 | 信封与红围巾 | 1038 | normal | 93.6 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「赵阿姨的」×4
  - 情节与已写章节重复 0.81 ≥ 0.62（撞上「老李与赵阿姨争夺一封可能涉及失踪孩子的信件，两人在冰台边…」）
  - [observe] 章内自我复读 4 句（如「照片上的男孩笑得灿烂，背后写着“赵建国”三个字…」）
  - [observe] 标题重复：「信封与红围巾」已存在
- 第 3 章：
  - 单条套路句式超限：「赵阿姨的」×6
  - [observe] 标题重复：「信封与红围巾」已存在
- 第 4 章：
  - 单条套路句式超限：「赵阿姨的」×3
  - narration_para_pct 25.9 低于目标 35.0
  - [observe] 标题重复：「信封与红围巾」已存在
- 第 5 章：
  - 单条套路句式超限：「赵阿姨的」×4
  - [observe] 标题重复：「信封与红围巾」已存在
- 第 6 章：
  - [observe] 标题重复：「信封与红围巾」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6084
chapter_chars_mean: 1014
chapter_chars_median: 1104
chapter_chars_cv: 0.22
paragraphs_mean: 29.3
dialogue_chars_pct: 19.1
dialogue_para_pct: 51.4
interiority_para_pct: 2.1
narration_para_pct: 46.6
turn_under20_pct: 96.5
turn_over200_pct: 0.0
attr_say_pct: 37.7
attr_adv_pct: 0.0
scenes_per_chapter: 1.3
dialogue_run_mean: 2.1
turn_len_median: 8
```

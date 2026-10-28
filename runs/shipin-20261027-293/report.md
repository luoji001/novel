# 红绸缠车门 生成报告

slug：`shipin-20261027-293`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6520
LLM 调用：57 次，累计 139.0 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铁锹砸向车门 | 595 | short | 39.1 | 0 |  | 1 |
| 2 | 铁锹撬开后备箱 | 1011 | normal | 35.5 | 0 |  | 2 |
| 3 | 铁锹撬开车厢盖 | 1238 | normal | 93.3 | 0 |  | 1 |
| 4 | 手机屏幕亮起 | 1430 | normal | 92.9 | 0 |  | 0 |
| 5 | 对讲机构成回声 | 1041 | normal | 92.1 | 0 |  | 0 |
| 6 | 铁锹撬开车厢盖 | 1199 | normal | 91.7 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 539 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章内自我复读 2 句（如「那是我同事的财物，你不能拿…」）
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）
- 第 3 章：
  - narration_para_pct 32.0 低于目标 35.0
- 第 6 章：
  - narration_para_pct 20.7 低于目标 35.0
  - dialogue_run_mean 4.6 高于目标 4.0
  - [observe] 标题重复：「铁锹撬开车厢盖」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6108
chapter_chars_mean: 1018
chapter_chars_median: 1055
chapter_chars_cv: 0.27
paragraphs_mean: 26.5
dialogue_chars_pct: 22.0
dialogue_para_pct: 58.3
interiority_para_pct: 1.1
narration_para_pct: 40.6
turn_under20_pct: 94.9
turn_over200_pct: 0.0
attr_say_pct: 30.7
attr_adv_pct: 21.6
scenes_per_chapter: 1.2
dialogue_run_mean: 2.5
turn_len_median: 10
```

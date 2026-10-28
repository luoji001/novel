# 二维码风波 生成报告

slug：`shipin-20261027-241`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7219
LLM 调用：57 次，累计 145.4 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 扫码守摊 | 808 | short | 100.0 | 0 |  | 1 |
| 2 | 扫码守摊 | 1444 | normal | 91.1 | 0 |  | 1 |
| 3 | 铁皮盒里的旧账 | 1243 | normal | 86.8 | 0 |  | 2 |
| 4 | 二维码的倾斜角度 | 1180 | normal | 91.4 | 0 |  | 1 |
| 5 | 扫码守摊 | 1337 | normal | 91.0 | 0 |  | 2 |
| 6 | 扫码守摊 | 1201 | normal | 36.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - narration_para_pct 23.1 低于目标 35.0
- 第 2 章：
  - [observe] 标题重复：「扫码守摊」已存在
- 第 3 章：
  - narration_para_pct 20.6 低于目标 35.0
  - dialogue_run_mean 6.8 高于目标 4.0
- 第 4 章：
  - 单条套路句式超限：「李大勇的」×3
- 第 5 章：
  - narration_para_pct 33.3 低于目标 35.0
  - [observe] 标题重复：「扫码守摊」已存在
- 第 6 章：
  - 单条套路句式超限：「王小伟的」×3
  - [observe] 章内自我复读 1 句（如「王小伟看着那袋米粉，眼底闪过一丝不易察觉的光亮…」）
  - [observe] 标题重复：「扫码守摊」已存在

## 整书结构指标

```
chapters: 6
total_chars: 6783
chapter_chars_mean: 1130
chapter_chars_median: 1146
chapter_chars_cv: 0.19
paragraphs_mean: 29.2
dialogue_chars_pct: 25.1
dialogue_para_pct: 61.5
interiority_para_pct: 1.7
narration_para_pct: 36.7
turn_under20_pct: 92.8
turn_over200_pct: 0.0
attr_say_pct: 32.5
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 3.2
turn_len_median: 10
```

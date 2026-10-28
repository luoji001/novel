# 胶片的归宿 生成报告

slug：`shipin-20261027-319`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5186
LLM 调用：57 次，累计 122.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 贴标签 | 325 | short | 18.0 | 0 |  | 3 |
| 2 | 钥匙与铁盒 | 1029 | normal | 92.4 | 0 |  | 0 |
| 3 | 红布条划过夕阳 | 1239 | normal | 91.6 | 0 |  | 0 |
| 4 | 放映机的光痕 | 795 | normal | 36.0 | 0 |  | 1 |
| 5 | 钥匙与胶片 | 1036 | normal | 90.6 | 0 |  | 2 |
| 6 | 铁盒坠地碎 glass | 756 | normal | 15.6 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

1. 第一章提到老周“锁上铁盒离开空荡的放映室”，但第六章提到老周“带着铁盒与镇长对峙”，说明铁盒在第一章后并未被锁上或遗失，存在前后矛盾。

2. 第三章提到老周“选择留下”，但第六章提到老周“带着铁盒与镇长对峙”，说明老周在第三章后并未真正留下，存在立场变化无明确交代。

3. 第四章提到“小林与他一同探寻其中的秘密”，但第三章未提及小林出现，且小林在第五章才被提及，存在人物出场时间线错乱。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 100.0 高于目标 90.0
  - [observe] 章节过短 263 < 597（本章目标 1087 字的 55%）
- 第 4 章：
  - [observe] 章节过短 737 < 870（本章目标 1582 字的 55%）
- 第 5 章：
  - 命中套话收尾句
  - [observe] 标题与《钥匙与铁盒》近似 0.60 ≥ 0.6（换个角度，别只换一个词）
- 第 6 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 97.1 高于目标 90.0
  - [observe] 章节过短 669 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 4695
chapter_chars_mean: 782
chapter_chars_median: 816
chapter_chars_cv: 0.39
paragraphs_mean: 29.8
dialogue_chars_pct: 18.3
dialogue_para_pct: 38.4
interiority_para_pct: 1.2
narration_para_pct: 60.5
turn_under20_pct: 91.5
turn_over200_pct: 0.0
attr_say_pct: 37.7
attr_adv_pct: 0.0
scenes_per_chapter: 2.3
dialogue_run_mean: 1.6
turn_len_median: 10
```

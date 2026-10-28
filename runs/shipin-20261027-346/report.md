# 铜钥 生成报告

slug：`shipin-20261027-346`
档位：视频分镜　闸门模式：observe
章数：6　总字数：5677
LLM 调用：57 次，累计 123.8 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 铜锈痕迹的摩挲 | 643 | short | 39.6 | 0 |  | 1 |
| 2 | 钥匙卡入铁门缝隙 | 900 | normal | 36.9 | 0 |  | 1 |
| 3 | 钥匙敲击箱体 | 958 | normal | 36.8 | 0 |  | 1 |
| 4 | 钥匙摩挲铜锈痕迹 | 1133 | normal | 8.9 | 0 |  | 2 |
| 5 | 水滴入裂痕 | 911 | normal | 17.6 | 0 |  | 4 |
| 6 | 擦拭眼镜的荧光纹 | 1126 | normal | 58.7 | 0 |  | 0 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - [observe] 章节过短 592 < 597（本章目标 1087 字的 55%）
- 第 2 章：
  - [observe] 章节过短 844 < 870（本章目标 1582 字的 55%）
- 第 3 章：
  - [observe] 章内自我复读 1 句（如「他说着往身后退了一步，靴底碾碎地上干枯的海藻…」）
- 第 4 章：
  - interiority_para_pct 13.0 高于目标 6.0
  - [observe] 章内自我复读 1 句（如「林婉清站起身，连衣裙随着动作飘动，露出小腿上淡褐…」）
- 第 5 章：
  - dialogue_chars_pct 0.0 低于目标 5.0
  - narration_para_pct 97.9 高于目标 90.0
  - [observe] 章内自我复读 2 句（如「水面泛起涟漪，映出窗外飘落的一片银杏叶…」）
  - [observe] 章节过短 766 < 870（本章目标 1582 字的 55%）

## 整书结构指标

```
chapters: 6
total_chars: 5255
chapter_chars_mean: 876
chapter_chars_median: 877
chapter_chars_cv: 0.21
paragraphs_mean: 24.2
dialogue_chars_pct: 7.5
dialogue_para_pct: 27.8
interiority_para_pct: 4.0
narration_para_pct: 68.2
turn_under20_pct: 100.0
turn_over200_pct: 0.0
attr_say_pct: 39.2
attr_adv_pct: 0.0
scenes_per_chapter: 1.8
dialogue_run_mean: 1.3
turn_len_median: 10
```

# 手套 生成报告

slug：`shipin-20261027-389`
档位：视频分镜　闸门模式：observe
章数：6　总字数：6220
LLM 调用：57 次，累计 127.1 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 钥匙转动的瞬间 | 756 | short | 93.6 | 0 |  | 0 |
| 2 | 砸碎公文夹 | 969 | normal | 58.4 | 0 |  | 0 |
| 3 | 整理胶片的午后 | 1014 | normal | 58.6 | 0 |  | 0 |
| 4 | 钥匙转动的瞬间 | 1106 | normal | 90.8 | 0 |  | 1 |
| 5 | 手套与胶片的对峙 | 1147 | normal | 92.4 | 0 |  | 0 |
| 6 | 胶片滑入黑暗的瞬间 | 1222 | normal | 34.3 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 4 章：
  - [observe] 标题重复：「钥匙转动的瞬间」已存在
- 第 6 章：
  - interiority_para_pct 8.7 高于目标 6.0
  - [observe] attr_adv_pct 100.0 > 18.0（结构塌缩）

## 整书结构指标

```
chapters: 6
total_chars: 5819
chapter_chars_mean: 970
chapter_chars_median: 997
chapter_chars_cv: 0.17
paragraphs_mean: 24.7
dialogue_chars_pct: 20.2
dialogue_para_pct: 39.3
interiority_para_pct: 2.4
narration_para_pct: 58.3
turn_under20_pct: 96.2
turn_over200_pct: 0.0
attr_say_pct: 28.8
attr_adv_pct: 19.9
scenes_per_chapter: 2
dialogue_run_mean: 1.6
turn_len_median: 10
```

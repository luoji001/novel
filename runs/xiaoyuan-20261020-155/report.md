# 磁带里的声音 生成报告

slug：`xiaoyuan-20261020-155`
档位：校园青春　闸门模式：observe
章数：9　总字数：21077
LLM 调用：100 次，累计 454.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 指尖触碰调令 | 1519 | short | 100.0 | 0 |  | 0 |
| 2 | 划掉名字的课表 | 3086 | normal | 85.7 | 0 |  | 2 |
| 3 | 磁带盒掉落瞬间 | 2392 | normal | 92.4 | 0 |  | 1 |
| 4 | 袖口的折痕 | 2740 | normal | 91.9 | 0 |  | 1 |
| 5 | 磁带标签飘向操场 | 2404 | normal | 90.1 | 0 |  | 2 |
| 6 | 触摸纸张的温度 | 2159 | normal | 90.9 | 0 |  | 1 |
| 7 | 袖口的折痕 | 2749 | normal | 91.9 | 0 |  | 2 |
| 8 | 调令的重量 | 2147 | normal | 78.8 | 0 |  | 3 |
| 9 | 指尖触碰通知书 | 1872 | short | 93.8 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「苏明岚的」×3
  - [observe] 章内自我复读 17 句（如「这一次，她写得更快了，像是要把所有的想法都塞进这…」）
- 第 3 章：
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「点了点头」×3、「带着一丝」×3
- 第 5 章：
  - 单条套路句式超限：「点了点头」×3
  - narration_para_pct 7.8 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「苏明岚的」×5
- 第 7 章：
  - 单条套路句式超限：「陆子墨的」×4
  - [observe] 标题重复：「袖口的折痕」已存在
- 第 8 章：
  - 单条套路句式超限：「点了点头」×3、「不仅仅是」×3、「知道自己」×3
  - dialogue_chars_pct 16.2 低于目标 20.0
  - [observe] 章内自我复读 24 句（如「陈老师的办公桌上堆满了文件，电脑屏幕上闪着蓝光，…」）
- 第 9 章：
  - narration_para_pct 10.0 低于目标 15.0
  - [observe] 标题与《指尖触碰调令》近似 0.62 ≥ 0.6（换个角度，别只换一个词）

## 整书结构指标

```
chapters: 9
total_chars: 19928
chapter_chars_mean: 2214
chapter_chars_median: 2228
chapter_chars_cv: 0.21
paragraphs_mean: 54.1
dialogue_chars_pct: 25.5
dialogue_para_pct: 67.0
interiority_para_pct: 13.2
narration_para_pct: 19.8
turn_under20_pct: 92.2
turn_over200_pct: 0.0
attr_say_pct: 31.3
attr_adv_pct: 4.7
scenes_per_chapter: 2.2
dialogue_run_mean: 3.6
turn_len_median: 9
```

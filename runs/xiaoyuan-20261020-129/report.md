# 颜料温度 生成报告

slug：`xiaoyuan-20261020-129`
档位：校园青春　闸门模式：observe
章数：9　总字数：21198
LLM 调用：100 次，累计 448.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 触碰名单边缘的手指 | 1283 | short | 98.8 | 0 |  | 0 |
| 2 | 校服外套的温度 | 2647 | normal | 92.4 | 0 |  | 1 |
| 3 | 颜料沾染的指尖 | 2664 | normal | 87.5 | 0 |  | 3 |
| 4 | 手指摩挲袖口褶皱 | 2893 | normal | 90.8 | 0 |  | 3 |
| 5 | 素描本的铅笔痕迹 | 2640 | normal | 84.2 | 0 |  | 3 |
| 6 | 颜料沾染的指尖 | 2805 | normal | 92.0 | 0 |  | 1 |
| 7 | 素描本的裂痕 | 2092 | normal | 84.9 | 0 |  | 4 |
| 8 | 手指摩挲课表边缘 | 2531 | normal | 92.0 | 0 |  | 1 |
| 9 | 颜料沾染的指尖 | 1634 | short | 91.5 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - 单条套路句式超限：「“我不知道」×3、「周子墨的」×3
- 第 3 章：
  - dialogue_chars_pct 19.4 低于目标 20.0
  - attr_adv_pct 14.3 高于目标 12.0
  - [observe] 章内自我复读 17 句（如「她拿出一张空白的宣纸，轻轻地铺平，然后拿起一支炭…」）
- 第 4 章：
  - 单条套路句式超限：「“我不知道」×6
  - narration_para_pct 8.6 低于目标 15.0
  - attr_adv_pct 14.3 高于目标 12.0
- 第 5 章：
  - 单条套路句式超限：「周子墨点」×4
  - dialogue_chars_pct 17.3 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「那是上周不小心扯下的，上面写着一些模糊的字迹，像…」）
- 第 6 章：
  - [observe] 标题重复：「颜料沾染的指尖」已存在
- 第 7 章：
  - dialogue_chars_pct 19.0 低于目标 20.0
  - attr_adv_pct 20.0 高于目标 12.0
  - [observe] 章内自我复读 16 句（如「陈老师走到他面前，手指轻轻碰了碰素描本的封皮，“…」）
  - [observe] 标题与《素描本的铅笔痕迹》近似 0.71 ≥ 0.6（换个角度，别只换一个词）
- 第 8 章：
  - 单条套路句式超限：「知道自己」×4
- 第 9 章：
  - narration_para_pct 5.7 低于目标 15.0
  - [observe] 章内自我复读 1 句（如「林夏的手指悬在画布上方，迟迟没有落下…」）
  - [observe] 标题重复：「颜料沾染的指尖」已存在

## 整书结构指标

```
chapters: 9
total_chars: 20088
chapter_chars_mean: 2232
chapter_chars_median: 2500
chapter_chars_cv: 0.24
paragraphs_mean: 53.4
dialogue_chars_pct: 26.6
dialogue_para_pct: 65.1
interiority_para_pct: 15.6
narration_para_pct: 19.3
turn_under20_pct: 89.7
turn_over200_pct: 0.0
attr_say_pct: 50.9
attr_adv_pct: 7.8
scenes_per_chapter: 2.3
dialogue_run_mean: 3.7
turn_len_median: 10
```

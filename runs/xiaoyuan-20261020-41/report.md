# 借条抽屉 生成报告

slug：`xiaoyuan-20261020-41`
档位：校园青春　闸门模式：observe
章数：9　总字数：20385
LLM 调用：100 次，累计 440.7 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 分科表边缘的指纹 | 1399 | short | 87.4 | 0 |  | 1 |
| 2 | 校服领口的折痕 | 2382 | normal | 44.2 | 0 |  | 4 |
| 3 | 借条抽屉的沉默 | 2887 | normal | 88.4 | 0 |  | 2 |
| 4 | 课表上的空白 | 2353 | normal | 91.1 | 0 |  | 1 |
| 5 | 纸飞机坠入余晖 | 2467 | normal | 37.5 | 0 |  | 3 |
| 6 | 自行车后座的温度 | 2532 | normal | 91.7 | 0 |  | 2 |
| 7 | 蓝色文件袋的重量 | 2326 | normal | 86.7 | 0 |  | 2 |
| 8 | 抽屉最底层的纸 | 2753 | normal | 85.7 | 0 |  | 2 |
| 9 | 分科表边缘的指纹 | 1277 | short | 92.2 | 0 |  | 1 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 14.5 低于目标 20.0
- 第 2 章：
  - 命中套话收尾句
  - 单条套路句式超限：「林小满站在」×4、「他知道这」×4
  - dialogue_chars_pct 13.3 低于目标 20.0
  - [observe] 章内自我复读 1 句（如「我不知道该怎么说……我只是觉得……有点奇怪…」）
- 第 3 章：
  - 单条套路句式超限：「周子航的」×9、「他知道这」×3、「林小满的」×3
  - dialogue_chars_pct 17.2 低于目标 20.0
- 第 4 章：
  - 单条套路句式超限：「周子航的」×4、「林小满的」×4
- 第 5 章：
  - 单条套路句式超限：「周子航的」×3
  - dialogue_chars_pct 12.5 低于目标 20.0
  - [observe] 章内自我复读 17 句（如「林小满看了他一眼，然后低下头继续盯着手中的书，“…」）
- 第 6 章：
  - 单条套路句式超限：「林小满点点」×4、「周子航的」×4
  - interiority_para_pct 6.7 低于目标 8.0
- 第 7 章：
  - dialogue_chars_pct 15.6 低于目标 20.0
  - narration_para_pct 13.9 低于目标 15.0
- 第 8 章：
  - 单条套路句式超限：「周子航的」×7、「带着一丝」×3
  - dialogue_chars_pct 15.4 低于目标 20.0
- 第 9 章：
  - [observe] 标题重复：「分科表边缘的指纹」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19480
chapter_chars_mean: 2164
chapter_chars_median: 2289
chapter_chars_cv: 0.25
paragraphs_mean: 42.1
dialogue_chars_pct: 18.0
dialogue_para_pct: 59.1
interiority_para_pct: 19.6
narration_para_pct: 21.3
turn_under20_pct: 92.0
turn_over200_pct: 0.0
attr_say_pct: 36.7
attr_adv_pct: 2.5
scenes_per_chapter: 2.3
dialogue_run_mean: 2.8
turn_len_median: 9
```

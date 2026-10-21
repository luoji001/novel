# 补课通知的张贴 生成报告

slug：`xiaoyuan-20261020-116`
档位：校园青春　闸门模式：observe
章数：9　总字数：20106
LLM 调用：100 次，累计 441.5 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 抚摸名单的指尖 | 1472 | short | 98.4 | 0 |  | 0 |
| 2 | 触摸照片的指尖 | 2702 | normal | 90.6 | 0 |  | 1 |
| 3 | 笔记本的裂痕 | 2533 | normal | 88.3 | 0 |  | 2 |
| 4 | 磁带的褶皱 | 2312 | normal | 84.5 | 0 |  | 2 |
| 5 | 脚印在台阶上延伸 | 2420 | normal | 92.5 | 0 |  | 2 |
| 6 | 拾起病历本的瞬间 | 2359 | normal | 55.0 | 0 |  | 2 |
| 7 | 电流声中的对话 | 2188 | normal | 89.9 | 0 |  | 2 |
| 8 | 值日表的签名 | 2568 | normal | 91.2 | 0 |  | 1 |
| 9 | 抚摸名单的指尖 | 1543 | short | 86.9 | 0 |  | 3 |

## 一致性检查（8B 产出，只作参考）

未发现

## 质量债（放行但未达标的项）

- 第 2 章：
  - dialogue_chars_pct 18.3 低于目标 20.0
- 第 3 章：
  - dialogue_chars_pct 18.7 低于目标 20.0
  - attr_adv_pct 12.5 高于目标 12.0
- 第 4 章：
  - 单条套路句式超限：「苏晓阳的」×5、「他知道自己」×4
  - [observe] 章内自我复读 36 句（如「他转过身，看见周老师正拿着一份文件朝这边走来，脚…」）
- 第 5 章：
  - 单条套路句式超限：「苏晓阳的」×3
  - narration_para_pct 11.7 低于目标 15.0
- 第 6 章：
  - 单条套路句式超限：「苏晓阳的」×6
  - dialogue_chars_pct 14.6 低于目标 20.0
- 第 7 章：
  - 单条套路句式超限：「陆子墨点」×3
  - [observe] 章内自我复读 20 句（如「陆子墨笑了，那是他第一次写歌词的时候，还在宿舍床…」）
- 第 8 章：
  - [observe] 章内自我复读 2 句（如「周老师站在走廊尽头，手里拿着值日表…」）
- 第 9 章：
  - dialogue_chars_pct 15.2 低于目标 20.0
  - narration_para_pct 13.0 低于目标 15.0
  - [observe] 标题重复：「抚摸名单的指尖」已存在

## 整书结构指标

```
chapters: 9
total_chars: 19080
chapter_chars_mean: 2120
chapter_chars_median: 2269
chapter_chars_cv: 0.2
paragraphs_mean: 47.4
dialogue_chars_pct: 22.5
dialogue_para_pct: 63.0
interiority_para_pct: 13.3
narration_para_pct: 23.8
turn_under20_pct: 90.3
turn_over200_pct: 0.0
attr_say_pct: 40.6
attr_adv_pct: 4.0
scenes_per_chapter: 2.7
dialogue_run_mean: 2.6
turn_len_median: 10
```

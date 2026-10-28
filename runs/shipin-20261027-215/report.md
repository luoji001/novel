# 雨靴风波 生成报告

slug：`shipin-20261027-215`
档位：视频分镜　闸门模式：observe
章数：6　总字数：7745
LLM 调用：57 次，累计 141.2 秒

## 逐章

| 章 | 标题 | 字数 | 档位 | 分 | 轮数 | 降级 | 质量债 |
|---|---|---|---|---|---|---|---|
| 1 | 雨靴与红围巾 | 876 | short | 91.2 | 0 |  | 3 |
| 2 | 报纸入袋 | 1412 | normal | 93.0 | 0 |  | 0 |
| 3 | 铁锹撞门 | 1254 | normal | 36.9 | 0 |  | 1 |
| 4 | 雨靴与铁锹 | 1636 | normal | 36.4 | 0 |  | 3 |
| 5 | 红围巾拂过疤痕 | 1228 | normal | 91.1 | 0 |  | 1 |
| 6 | 雨靴与塑料袋 | 1333 | normal | 88.7 | 0 |  | 2 |

## 一致性检查（8B 产出，只作参考）

1. 第一章提到“李阿姨”，但后续章节中人物称呼变为“李阿姨”与“赵建国”、“物业管理员”，未出现“李阿姨”与其他人物的明确称呼一致性，存在称呼不一致问题。

2. 第二章提到“赵建国将收集的旧报纸整理后送至物业”，但第三章提到“李阿姨与赵建国因一双婚鞋发生争执”，此处“婚鞋”与前文“雨靴”混淆，存在物品名称不一致问题。

3. 第四章提到“物业管理员调解李阿姨与王大爷因一双黑色雨靴引发的争执”，但前文未出现“王大爷”这一人物，存在人物突然出现的问题。

4. 第五章提到“赵建国帮助李阿姨找回遗失的婚鞋”，但前文多次提到“雨靴”而非“婚鞋”，存在物品名称不一致问题。

5. 第六章提到“李阿姨与赵建国因一双遗失的婚鞋产生交集”，但前文多次使用“雨靴”而非“婚鞋”，存在物品名称不一致问题。

## 质量债（放行但未达标的项）

- 第 1 章：
  - dialogue_chars_pct 54.7 高于目标 45.0
  - narration_para_pct 11.5 低于目标 35.0
  - dialogue_run_mean 7.3 高于目标 4.0
- 第 3 章：
  - [observe] attr_adv_pct 25.0 > 18.0（结构塌缩）
- 第 4 章：
  - narration_para_pct 18.8 低于目标 35.0
  - dialogue_run_mean 5.2 高于目标 4.0
  - [observe] 章内自我复读 8 句（如「物业管理员沉默片刻，忽然掏出一张皱巴巴的纸条，上…」）
- 第 5 章：
  - narration_para_pct 34.6 低于目标 35.0
- 第 6 章：
  - narration_para_pct 28.9 低于目标 35.0
  - dialogue_run_mean 5.4 高于目标 4.0

## 整书结构指标

```
chapters: 6
total_chars: 7233
chapter_chars_mean: 1206
chapter_chars_median: 1202
chapter_chars_cv: 0.2
paragraphs_mean: 34.2
dialogue_chars_pct: 31.8
dialogue_para_pct: 68.0
interiority_para_pct: 1.3
narration_para_pct: 30.6
turn_under20_pct: 85.6
turn_over200_pct: 0.0
attr_say_pct: 35.4
attr_adv_pct: 4.0
scenes_per_chapter: 2.2
dialogue_run_mean: 4.1
turn_len_median: 12
```

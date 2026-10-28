"""规则式质量校验层。

三层结构：
  metrics.py  — vendor 自生产线，字节级一致，不要手改（见 VENDOR.md）
  rules.py    — 原语：正则、中文数字、相似度、模板匹配
  checks.py   — 策略：硬拦 / 标题 / 软警告 三组 + 规则打分
"""

from .checks import load_blacklist, score_text, validate
from .rules import Gates, Verdict, extract_title, normalize_prose, retitle, to_cn

__all__ = [
    "Gates", "Verdict", "validate", "score_text", "load_blacklist",
    "retitle", "extract_title", "to_cn", "normalize_prose",
]

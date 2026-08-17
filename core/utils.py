"""Small shared utilities for UltraJarvis."""

from __future__ import annotations

import re
import time
from typing import Union


def slugify(text: str, *, max_len: int = 40) -> str:
    """Turn text into a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = text.strip("_")
    return text[:max_len] or "item"


def human_seconds(seconds: Union[int, float]) -> str:
    """Format seconds into a short human string (e.g. 1m, 1h 5m)."""
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    minutes, sec = divmod(seconds, 60)
    if minutes < 60:
        return f"{minutes}m" if sec == 0 else f"{minutes}m {sec}s"
    hours, minutes = divmod(minutes, 60)
    if hours < 24:
        parts = [f"{hours}h"]
        if minutes:
            parts.append(f"{minutes}m")
        return " ".join(parts)
    days, hours = divmod(hours, 24)
    parts = [f"{days}d"]
    if hours:
        parts.append(f"{hours}h")
    return " ".join(parts)


def now_ts() -> float:
    return time.time()

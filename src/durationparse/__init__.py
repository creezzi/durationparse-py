"""Human friendly durations."""
from __future__ import annotations

import re

__all__ = ["parse", "format_duration"]

_UNITS = {
    "ms": 0.001, "s": 1, "sec": 1, "m": 60, "min": 60, "h": 3600, "hr": 3600,
    "d": 86400, "day": 86400, "days": 86400, "w": 604800, "wk": 604800,
    "hours": 3600, "hour": 3600, "minutes": 60, "minute": 60, "seconds": 1, "second": 1,
}
_PART = re.compile(r"\s*(\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s*")


def parse(text: str) -> float:
    """'1h30m', '90 min', '1.5d', '2w 1d' -> seconds. A bare number is seconds."""
    text = text.strip().lower()
    if not text:
        raise ValueError("empty duration")
    if re.fullmatch(r"\d+(\.\d+)?", text):
        return float(text)
    pos, total = 0, 0.0
    while pos < len(text):
        m = _PART.match(text, pos)
        if not m or m.group(2) not in _UNITS:
            raise ValueError(f"cannot parse duration: {text!r}")
        total += float(m.group(1)) * _UNITS[m.group(2)]
        pos = m.end()
    return total


def format_duration(seconds: float) -> str:
    seconds = int(round(seconds))
    if seconds < 0:
        return "-" + format_duration(-seconds)
    if seconds == 0:
        return "0s"
    parts = []
    for name, size in (("d", 86400), ("h", 3600), ("m", 60), ("s", 1)):
        qty, seconds = divmod(seconds, size)
        if qty:
            parts.append(f"{qty}{name}")
    return " ".join(parts)

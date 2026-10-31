import pytest

from durationparse import format_duration, parse


@pytest.mark.parametrize("text,seconds", [
    ("90", 90), ("1h30m", 5400), ("1h 30m", 5400), ("90 min", 5400), ("1.5d", 129600),
    ("2w 1d", 1296000), ("250ms", 0.25), ("2 hours 5 minutes", 7500), ("  5S ", 5),
])
def test_parse(text, seconds):
    assert parse(text) == pytest.approx(seconds)


@pytest.mark.parametrize("bad", ["", "abc", "5x", "h", "1h 30", "1h-30m"])
def test_parse_errors(bad):
    with pytest.raises(ValueError):
        parse(bad)


@pytest.mark.parametrize("seconds,text", [
    (0, "0s"), (59, "59s"), (60, "1m"), (3661, "1h 1m 1s"), (93784, "1d 2h 3m 4s"), (-90, "-1m 30s"),
])
def test_format(seconds, text):
    assert format_duration(seconds) == text


def test_roundtrip():
    for s in (1, 59, 3600, 90061):
        assert parse(format_duration(s)) == s

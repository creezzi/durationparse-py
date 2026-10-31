# durationparse

Parse human durations like '1h30m' into seconds and format seconds back into text.

## Usage

```python
from durationparse import parse, format_duration

parse("1h 30m")             # -> 5400.0
format_duration(93784)      # -> "1d 2h 3m 4s"
```

## Test

```bash
pip install pytest && pytest
```

## License

MIT

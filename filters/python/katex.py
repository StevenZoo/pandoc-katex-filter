#!/usr/bin/env python3

from pandocfilters import RawInline, toJSONFilter
from client import render


def katex(key, value, format, meta):
    if key != "Math" or len(value) < 2:
        return None

    formatter, tex = value
    display = formatter['t'] == 'DisplayMath'

    html = render(tex, display)

    if html is not None:
        return RawInline('html', html)


if __name__ == '__main__':
    toJSONFilter(katex)

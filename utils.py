import sys
from typing import Callable, Dict, TextIO, Tuple


def possible(d: Dict[str, Tuple[int, Callable]], n: str) -> int:
    """Checks if the string is possible to be an operator.

    Args:
        - `d` (`Dict[str, Tuple[int, Callable]]`): All the operators.
        - `n` (`str`): The input as of now.

    Returns:
        - `int`: `2` if there is an exact same operator, `1` if possible,
        and `0` if not possible.
    """
    if n in d:
        return 2
    if not n and d:
        return 1
    for x in d:
        if x.startswith(n):
            return 1
    return 0


def _debug(*s, sep: str = ' ', file: TextIO = sys.stdout):
    ss = sep.join((str(x) for x in s)).split('\n')
    for s in ss:
        print('\x1b[33mDEBUG\x1b[0m: ', file=file, end='')
        print(s)

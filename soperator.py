import math
from typing import Callable

__all__ = ['SOperator']


class SOperator:
    FUNCTIONS = {
        '+': (2, lambda x, y: x + y, 2),
        '-': (2, lambda x, y: x - y, 2),
        '*': (2, lambda x, y: x * y, 3),
        '/': (2, lambda x, y: x / y, 3),
        '%': (2, lambda x, y: x % y, 3),
        '^': (2, lambda x, y: x ** y, 5),
        'sin': (1, math.sin, 50),
        'cos': (1, math.cos, 50),
        'tan': (1, math.tan, 50),
        'asin': (1, math.asin, 50),
        'acos': (1, math.acos, 50),
        'atan': (1, math.atan, 50),
        'dr': (1, math.radians, 50),
        'rd': (1, math.degrees, 50),
        'sqrt': (1, math.sqrt, 50),
        'sta': (1, lambda x: setattr(SOperator, 'REGISTER_A', x) or x),
        'lda': (),
        'pi': (0, lambda: math.pi, 99),
        'e': (0, lambda: math.e, 99),
    }

    REGISTER_A = ...

    def __init__(self, c: str):
        if c not in self.__class__.FUNCTIONS:
            raise ValueError('Operator ‘%s’ not found' % c)
        self.c: str = c
        self.f: Callable = self.__class__.FUNCTIONS[c][1]

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

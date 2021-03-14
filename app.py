from exceptions import InputError
from soperator import SOperator
from stack import Stack
from utils import _debug, possible
from queue import Queue

if __name__ == '__main__':
    from argparsing import parse

F = SOperator.FUNCTIONS


def main(i: str = None, debug=False):
    if i is None:
        i = input()
    q = Queue()
    n = ''
    isnum = False
    haspoint = False
    for c in i:
        if c.isdigit():
            if n and not isnum:
                if possible(F, n) != 2:
                    raise InputError
                if debug:
                    _debug('PUT', n)
                q.put(n)
                n = ''
            isnum = True
            n += c
        elif c == '.':
            if not isnum:
                raise InputError('Decimal point on non-number')
            if haspoint:
                raise InputError('A number has multiple decimal points')
            n += '.'
            haspoint = True
        elif c == ' ':
            if n:
                if isnum:
                    if debug:
                        _debug('PUT', n)
                    q.put(int(n) if n.isdigit() else float(n))
                else:
                    if debug:
                        _debug('PUT', n)
                    q.put(n)
                n = ''
                isnum = False
                haspoint = False
        else:
            if isnum:
                if debug:
                    _debug('PUT', n)
                q.put(int(n) if n.isdigit() else float(n))
                n = ''
                isnum = False
                haspoint = False
            p = possible(F, n + c)
            if p == 2:
                if debug:
                    _debug('PUT', n + c)
                q.put(n + c)
                n = ''
            elif p == 1:
                n += c
            else:
                p = possible(F, n)
                if p == 2:
                    if debug:
                        _debug('PUT', n)
                    q.put(n)
                    n = c
                elif p == 0:
                    raise RuntimeError('???!')
    if n:
        if isnum:
            if debug:
                _debug('PUT', n)
            q.put(int(n) if n.isdigit() else float(n))
        else:
            if debug:
                _debug('PUT', n)
            q.put(n)
    s = Stack()
    while not q.empty():
        x = q.get()
        if x in F:
            if len(s) < F[x][0]:
                raise InputError('Operator ‘%s’ needs %i operands, got only %i' % (
                    x, F[x][0], len(s)))
            a = []
            for _ in range(F[x][0]):
                a.insert(0, s.get())
            s.put(F[x][1](*a))
        else:
            s.put(x)
    if debug:
        _debug(s)
    if s.empty():
        raise InputError('Final answer is None')
    print(s.top())


if __name__ == '__main__':
    parse()

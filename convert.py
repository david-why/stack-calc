from exceptions import InputError
from soperator import SOperator
from stack import Stack
from utils import _debug, possible

F = SOperator.FUNCTIONS


def convert(debug=False, squish=False):
    s1 = Stack()
    s2 = Stack()
    i = input()
    n = ''
    isnum = False
    haspoint = False
    for c in i:
        if c.isdigit():
            if n and not isnum:
                if possible(F, n) != 2:
                    if n == '(':
                        s1.push('(')
                    elif n == ')':
                        while s1.top() != '(':
                            s2.push(s1.pop())
                        s1.pop()
                    else:
                        raise InputError
                while not (s1.empty() or s1.top() == '(' or F[s1.top()][2] <= F[n][2]):
                    if debug:
                        _debug('S12 "?" !num', s1.top())
                    s2.push(s1.pop())
                s1.push(n)
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
                        _debug('PUT " " num', n)
                    s2.push(int(n) if n.isdigit() else float(n))
                else:
                    if debug:
                        _debug('PUT " " !num', n)
                    if possible(F, n) != 2:
                        if n == '(':
                            s1.push('(')
                        elif n == ')':
                            while s1.top() != '(':
                                s2.push(s1.pop())
                            s1.pop()
                        else:
                            raise InputError
                    while not (s1.empty() or s1.top() == '(' or F[s1.top()][2] <= F[n][2]):
                        if debug:
                            _debug('S12 " " !num', s1.top())
                        s2.push(s1.pop())
                    s1.push(n)
                n = ''
                isnum = False
                haspoint = False
        else:
            if isnum:
                if debug:
                    _debug('PUT "*" num', n)
                s2.put(int(n) if n.isdigit() else float(n))
                n = ''
                isnum = False
                haspoint = False
            p = possible(F, n + c)
            if p == 2:
                if debug:
                    _debug('PUT "*" !num', n + c)
                while not (s1.empty() or s1.top() == '(' or F[s1.top()][2] <= F[n + c][2]):
                    if debug:
                        _debug('S12 "*" !num', s1.top())
                    s2.push(s1.pop())
                s1.push(n + c)
                n = ''
            elif p == 1:
                n += c
            else:
                if c == '(':
                    s1.push('(')
                elif c == ')':
                    while s1.top() != '(':
                        s2.push(s1.pop())
                    s1.pop()
                else:
                    p = possible(F, n)
                    if p == 2:
                        if debug:
                            _debug('PUT', n)
                        while not (s1.empty() or s1.top() == '(' or F[s1.top()][2] <= F[n][2]):
                            if debug:
                                _debug('S12', s1.top())
                            s2.push(s1.pop())
                        s1.push(n)
                        n = c
                    elif p == 0:
                        raise RuntimeError('???!')
    if n:
        if isnum:
            if debug:
                _debug('PUT "n" num', n)
            s2.push(int(n) if n.isdigit() else float(n))
        else:
            if debug:
                _debug('PUT "n" !num', n)
            while not (s1.empty() or s1.top() == '(' or F[s1.top()][2] <= F[n + c][2]):
                if debug:
                    _debug('S12 "*" !num', s1.top())
                s2.push(s1.pop())
            s1.push(n)
    while not s1.empty():
        s2.push(s1.pop())
    if debug:
        _debug(s2)
    if not squish:
        return ' '.join((str(x) for x in s2.s))

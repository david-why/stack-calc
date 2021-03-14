from soperator import SOperator


class NoOperand(SOperator):
    FUNCTIONS = {
        x: SOperator.FUNCTIONS[x]
        for x in SOperator.FUNCTIONS
        if SOperator.FUNCTIONS[x][0] == 0
    }

    __repr__ = lambda self: str(self())


class SingleOperand(SOperator):
    FUNCTIONS = {
        x: SOperator.FUNCTIONS[x]
        for x in SOperator.FUNCTIONS
        if SOperator.FUNCTIONS[x][0] == 1
    }


class DoubleOperand(SOperator):
    FUNCTIONS = {
        x: SOperator.FUNCTIONS[x]
        for x in SOperator.FUNCTIONS
        if SOperator.FUNCTIONS[x][0] == 2
    }


if __name__ == '__main__':
    o = NoOperand('e')
    print(o)

from by_operands import DoubleOperand, NoOperand, SingleOperand, SOperator


def new_operator(s: str) -> SOperator:
    if s not in SOperator.FUNCTIONS:
        raise ValueError('Operator ‘%s’ not found' % s)
    x = SOperator.FUNCTIONS[s]
    if x[0] == 0:
        return NoOperand(s)
    elif x[0] == 1:
        return SingleOperand(s)
    elif x[0] == 2:
        return DoubleOperand(s)
    else:
        raise RuntimeError("?????!")

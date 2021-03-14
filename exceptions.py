class InputError(ArithmeticError):
    """The input to the calculator/converter is wrong"""

    def __init__(self, *args):
        if not args:
            super().__init__('The input to the calculator/converter is wrong')
        else:
            super().__init__(*args)

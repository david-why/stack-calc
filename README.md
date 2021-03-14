# Stack-Calc
A calculator based on Python's `list`-like stack.
## Usage
 1. Make sure `python==3.8` is installed on your computer.
 2. Run `/path/to/python app.py` in root folder of project.
 3. Enter arguments as needed.
## Installation
No need to install! Just use it!

If you *have to* install it, just run `sh install.sh` (or `make install`). It will copy all `.py` files to `~/.local/lib/python3.8/site-packages/ctack-calc`. Use `sh uninstall.sh` (or `make uninstall`) to uninstall.
## Description of files
 - `app.py`: The main application.
 - `argparsing.py`: The argument parsing module meant to be imported by `app.py` to parse command-line arguments.
 - `by_operands.py`: The module that seperates `SOperator` into `NoOperand`, `SingleOperand`, and `DoubleOperand`.
 - `convert.py`: The module that converts between [postfix and infix expressions](#stack-calc).
 - `exceptions.py`: The module that defines `InputError` for the calculator.
 - `new_operator.py`: The module that defines function `new_operator` for creating an operator.
 - `soperator.py`: The module that defines class `SOperator` that represents a stack operator. (Pretty cool name, huh?)
 - `stack.py`: The module that defines class `Stack` that imitates a stack that is powered by a `list`.
 - `utils.py`: The module that defines some utilities used in the application.

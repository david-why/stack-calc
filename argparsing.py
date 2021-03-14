import click


@click.group(context_settings={'help_option_names': ['--help', '-h']})
@click.option('--postfix/--infix', '-p/-i', is_flag=True, help='Whether the expression input is a postfix '
              'expression or infix expression. [default: --postfix]', default=True)
@click.option('--debug', is_flag=True)
def parse(**kwargs):
    pass


@parse.command('calc', help='Run the calculator on the input expression.')
@click.option('--postfix/--infix', '-p/-i', is_flag=True, help='Whether the expression input is a postfix '
              'expression or infix expression. [default: --postfix]', default=True)
@click.option('--debug', is_flag=True)
def calc(postfix=True, debug=False):
    import app
    if postfix:
        app.main(input(), debug)
    else:
        from convert import convert as do_convert
        app.main(do_convert(postfix), debug)


@parse.command('convert', help='Convert between postfix and infix expressions.')
@click.option('--postfix/--infix', '-p/-i', is_flag=True, help='Whether the expression input is a postfix '
              'expression or infix expression. [default: --postfix]', default=True)
@click.option('--debug', is_flag=True)
@click.option('--squish', '-s', is_flag=True, help='Whether to squish the output or not. [default: False]', default=False)
def convert(postfix=True, debug=False, squish=False):
    from convert import convert as do_convert
    print(do_convert(postfix, debug, squish))


if __name__ == '__main__':
    parse()

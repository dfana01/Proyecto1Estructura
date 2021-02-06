import sys


def op_sum(n1, n2):
    return n1 + n2


def op_subtract(n1, n2):
    return n1 - n2


def op_multiplication(n1, n2):
    return n1 * n2


def op_division(n1, n2):
    return n1 / n2


def op_and(n1, n2):
    return float(int(n1) and int(n2))


def op_or(n1, n2):
    return float(int(n1) or int(n2))


operators = {
    "+": lambda x, y: op_sum(x, y),
    "-": lambda x, y: op_subtract(x, y),
    "*": lambda x, y: op_multiplication(x, y),
    "/": lambda x, y: op_division(x, y),
    "and": lambda x, y: op_and(x, y),
    "or": lambda x, y: op_or(x, y),
}


def calculate(*args):
    try:
        acu = float(int(args[0], 2))
        for idx in range(1, len(args)):
            if idx % 2 != 0:
                op = args[idx]
                n = float(int(args[idx + 1], 2))
                acu = operators[op](acu, n)
        return acu
    except Exception:
        raise ValueError(r"""
            Malformed exception please check if your input complies the format 
            Format: calculator <binary-number> <+ | - | * | / | and | or> <binary-number> [<+ | - | * | / | and | or> <binary-number>]
        """)


def execute(*args):
    return r"""
    Welcome to the calculator, with this CLI util you can do: 
    - sum (+) 
    - subtraction (-) 
    - multiplication (*) 
    - division (/) 
    - and (and) 
    - or (or) 

    Format: calculator <binary-number> <+ | - | * | / | or | and> <binary-number> [<+ | - | * | / | and | or> <binary-number>] 

    Author: <Dante Fana Badia>dfana@dfb.com.do
    """ if not len(args) else r"Thanks for using the calculator, result: {}".format(calculate(*args))


def main(*args):
    print(execute(*args))


if __name__ == '__main__':
    main(*sys.argv[1:])

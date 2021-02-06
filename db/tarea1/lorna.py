# Calculadora

def sumar(n, n1):
    return n + n1


def resta(n, n1):
    return n - n1


def multi(n, n1):
    return n * n1


def divi(n, n1):
    return n / n1


def a(n, n1):
    return n & n1


def o(n, n1):
    return n | n1


def text_show():
    print("Calculadora Binaria\nOperadores:")
    print(
        "Suma = '+' \n Resta = '-'\n Multiplicacion = '*'\n Division = '/'\n And = 'a' o 'A'\n Or = 'o' o 'O'\n Total "
        "= '='")

def calculate(op,n1,n2):
    r = 0
    if op == "+":
        r = sumar(n1,n2)

    elif op == "-":
        r = resta(n1,n2)

    elif op == "*":
        r = multi(n1,n2)

    elif op == "/":
        r = divi(n1,n2)

    elif op == "a" or op == "A":
        r = a(n1,n2)

    elif op == "o" or op == "O":
        r = o(n1,n2)

    return  r

def principal():
    n = int(input("Ingrese el valor en binario:"), 2)
    op = input("Ingrese operador:")

    while op != "=":

        n1 = int(input("Ingrese el valor en binario:"), 2)

        n = calculate(op,n,n1)

        op = input("Ingrese operador:")

    print(n)


if __name__ == '__main__':
    principal()

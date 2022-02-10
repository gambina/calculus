def add(a, b):
    return a+b


def substraction(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divive(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a/b

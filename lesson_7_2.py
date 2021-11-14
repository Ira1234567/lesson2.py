def arithmetic(a, b, c):
    a = int(a)
    b = int(b)
    if c == "+":
        return a+b
    elif c == "-":
        return a-b
    elif c == "*":
        return a*b
    elif c == "/":
        return a/b
    else:
        return "Неизвестная операция"


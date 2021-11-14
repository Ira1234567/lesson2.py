def arithmetic(a, b, c):
    a = int(a)
    b = int(b)
    if c == "+":
        print(a+b)
    elif c == "-":
        print(a-b)
    elif c == "*":
        print(a*b)
    elif c == "/":
        print(a/b)
    else:
        print("Неизвестная операция")
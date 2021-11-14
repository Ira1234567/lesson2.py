def function_1(a):
    a = [i for i in [int(i) for i in str(a)] if i != 0]
    b = 1
    for i in a:
       b *= i
    print(b)



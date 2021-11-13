a = set([int(i) for i in input()])
b = set([int(i) for i in input()])
c = {*a, *b}
if c == a:
    print("a является суперсетом для b")
else:
    print("a не является суперсетом для b")
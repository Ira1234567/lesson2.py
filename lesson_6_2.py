a = set([int(i) for i in input()])
b = set([int(i) for i in input()])
print(a)
print(b)
if a >= b:
   print("a является суперсетом для b")
else:
    print("a не является суперсетом для b")
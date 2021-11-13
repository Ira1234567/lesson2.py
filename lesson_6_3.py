import random
import string
a = {}
for i in [random.choice(string.ascii_letters) for _ in range(5)]:
    a[i] = random.randint(1,9)
print(a)
b = {}
for i in [random.choice(string.ascii_letters) for _ in range(5)]:
    b[i] = random.randint(1,50)
print(b)
c = {}
for key in a:
    if key in b:
        if a.get(key)>b.get(key):
            c[key] = a.get(key)
        else:
            c[key] = b.get(key)
    else:
        c[key] = a.get(key)
for key in b:
    if key in a:
        ...
    else:
        c[key] = b.get(key)
print(c)
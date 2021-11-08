import random
a = [random.randint(1,5) for _ in range(5)]
b = [random.randint(1,5) for _ in range(6)]
a.extend(b)
print(len([i for i in a if a.count(i)==1]))





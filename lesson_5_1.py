import random
a = [random.randint(1,5) for _ in range(5)]
b = [random.randint(1,5) for _ in range(6)]
print(len([i for i in a if i not in b])+len([i for i in b if i not in a]))

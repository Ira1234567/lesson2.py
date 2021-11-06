import random
print(len([i for i in [random.randint(1,9) for _ in range(15)] if i in [random.randint(1,9) for _ in range(20)]]))

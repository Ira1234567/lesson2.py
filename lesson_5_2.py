a = [int(i) for i in input("Введите список: ")]
print(a)
b = 0
for i in range(0, len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        b = b+1
print(b)
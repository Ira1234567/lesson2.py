a = [int(i) for i in input("Рост людей в строю: ").split()]
a.sort(reverse=True)
print(a)
X = int(input("Рост Пети: "))
b = 0
while len(a)>b and X<=a[b]:
    b = b+1
print(b+1)
a = int(input("Введите число: "))

b = int(a % 10)

c = int(a - b)


d = int((c % 100) / 10)

f = int((a - b - (d*10)) / 100)

g = int(b*100+d*10+f)

print(g)











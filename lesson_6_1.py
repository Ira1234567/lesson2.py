a = input("Введите текст: ")
a = list(a.split())
b = {}
for i in a:
    b[i] = a.count(i)
print(b)
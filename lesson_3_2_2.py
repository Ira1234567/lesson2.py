a = input("Введите строку/слово/число: ")

b = "Это строка в которую {} новую строку".format(a)

print(b)

c = b.replace(a,"замена в строке")

print(c)

print(len(b))

if "строка" in b:
    print("ДА")
else:
    print("Нет")
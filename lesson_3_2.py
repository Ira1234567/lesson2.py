a = input("Введите строку/слово/число: ")

b = "Это строка в которую {} новую строку".format(a)

print(b)

c = "Это строка в которую {} новую строку".format("замена в строке")

print(c)

print(len(b))

if "строка" in "Это строка в которую {} новую строку":
    print("ДА")
else:
    print("Нет")

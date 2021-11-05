a = int(input("Введите высоту строки "))
for ch in [i for i in range(a+1)]:
        print(" " * int(3*(2*(a+1)-1-2*ch-1)/2)," * " * int(2*ch-1)," " * int(3*(2*(a+1)-1-2*ch-1)/2))

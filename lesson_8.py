def login(username, password):
    if len(password) >= 4 and len(username) >= 4:
        return True
    else:
        return False


def check_password(username, password):
    usernames_and_passwords = {'name1': '1234', 'name2': '2345', 'name3': '3456', 'name4': '4567'}
    if username in usernames_and_passwords and usernames_and_passwords[username] == password:
        return True
    else:
        return False


def authenticate(func1, func2):
    if func1 == True and func2 == True:
        return True
    else:
        return False

a = 3
while a >=1:
    username_1 = (str(input("Введите имя пользователя: ")))
    password_1 = (str(input("Введите пароль: ")))
    if authenticate(login(username_1, password_1), check_password(username_1, password_1)) == True:
        print("Вы в системе!")
        break
    else:
        if a > 1:
            print("Не правильное имя или пароль. У вас осталось ", a-1, " попыток")
        else:
            print("Попытки истекли!")
    a -= 1
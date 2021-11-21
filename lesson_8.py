def decorator1(funk1):
    def funk2(check_password, authenticate):
        funk1
        def check_password(username, password):
            usernames_and_passwords = {'name1': '1234', 'name2': '2345', 'name3': '3456', 'name4': '4567'}
            if username in usernames_and_passwords and usernames_and_passwords[username] == password:
                return True
            else:
                return False
        def authenticate():
            return True
        if check_password(username1, password1) == True and authenticate() == True:
            return True
    return funk2

@decorator1
def login(username, password):
    if len(password) >= 4 and len(username) >= 4:
        return True
    else:
        return False

a = 3
while a >=1:
    username1 = input("Введите имя пользователя: ")
    password1 = input("Введите пароль: ")
    if login(username1, password1) == True:
        print("Вы в системе!")
        break
    else:
        if a > 1:
            print("Не правильное имя или пароль. У вас осталось ", a - 1, " попыток")
        else:
            print("Попытки истекли!")
    a -= 1

import datetime

def lock_out():
    last_failed_attempt = datetime.datetime(2021, 12, 14, 18, 48, 30)
    if datetime.datetime.now() <= last_failed_attempt + datetime.timedelta(minutes=5):
        return False


def check_password(username, password):
    usernames_and_passwords = {'name1': '1234', 'name2': '2345', 'name3': '3456', 'name4': '4567'}
    if username in usernames_and_passwords and usernames_and_passwords[username] == password:
        return True


def authenticate():
    return True



def decorator1(func1):
    def func2(username1, password1):
     if check_password(username1, password1) == True and authenticate() == True:
      return True
      return func1(username1, password1)
    return func2

@decorator1
def login(username, password):
    print('login done')
    return True

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--username', dest='username1')
parser.add_argument('--password', dest='password1')
args = parser.parse_args()
username1 = args.username1
password1 = args.password1
if username1 == None and password1 != None:
    username1 = input("Введите имя пользователя ")
elif password1 == None and username1 != None:
    password1 = input("Введите пароль ")

a = 3
while a >=1:
    if lock_out() == False:
       print("Вы заблокированы! Следующая попытка через 5 мин.")
       break
    elif login(username1, password1) == True:
            print("Вы в системе!")
            break
    else:
        a-=1
        username1 = input("Введите имя пользователя ")
        password1 = input("Введите пароль ")
        if login(username1, password1) == True:
            print("Вы в системе!")
            break
        elif a > 1:
            print("Не правильное имя или пароль. У вас осталось ", a - 1, " попыток")
        else:
            print("Попытки истекли!")
    a -= 1
class UserDoesNotExist(Exception):
    pass

def check_password(username, password):
    usernames_and_passwords = {'name1': '1234', 'name2': '2345', 'name3': '3456', 'name4': '4567'}
    try:
        if username not in usernames_and_passwords:
            raise UserDoesNotExist
    except UserDoesNotExist:
        print("User does not exist")
    else:
        if usernames_and_passwords[username] == password:
            return True
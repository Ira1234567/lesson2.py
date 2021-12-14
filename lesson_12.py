
import json

def decorator1(func1):
    def func2(username, password):
      user_data = [username, password]
      with open('new_file', 'w') as f:
        json.dump(user_data, f)
        f.close()
      return func1(username, password)
    return func2

@decorator1
def login(username, password):
    if len(password) >= 4 and len(username) >= 4:
        return username, password





login('name1','1234')




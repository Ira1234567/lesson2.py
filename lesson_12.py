
import json

def login(username, password):
    if len(password) >= 4 and len(username) >= 4:
        user_data = [username, password]
        with open('new_file', 'w') as f:
          json.dump(user_data,f)
        f.close()


login('name1','1234')




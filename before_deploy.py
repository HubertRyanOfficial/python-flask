import requests
import json
from configure_user_blend import users_blend_path

def main():
    res = requests.get("https://python-flask-e9bh.onrender.com/users/")
    data_users = res.json()

    with open(users_blend_path, 'w') as json_file:
        json.dump(data_users, json_file, indent=4)

    print('Success persisting data from users.\n')


main()

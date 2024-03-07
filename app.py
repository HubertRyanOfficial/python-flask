import json
import requests
from flask import Flask, jsonify
from configure_user_blend import load_users_data, users_blend_path
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix='/users')

@app.route('/')
def index():
    all_users = load_users_data()
    return jsonify({'message': 'Nice! You\'re using Oddity database.', 'total_users': len(all_users)})


if __name__ == "__main__":
    app.run(debug=True)



def main():
    res = requests.get("https://python-flask-e9bh.onrender.com/users/")
    data_users = res.json()
    data_old_users = load_users_data()

    if(len(data_users) > len(data_old_users)):
         with open(users_blend_path, 'w') as json_file:
            json.dump(data_users, json_file, indent=4)

    print('Success persisting data from users.\n')


main()

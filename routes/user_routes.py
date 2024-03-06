import json
from flask import Blueprint, jsonify, request
from configure_user_blend import load_users_data, users_blend_path

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/', methods=['GET', 'POST'])
@user_routes.route('/<username>?', methods=['DELETE'])
def get_users(username=None):
    if request.method == 'GET':
        data = load_users_data()

        return jsonify(data), 200
    if(request.method == 'POST'):
        new_user_data = request.get_json()

        old_users_list = load_users_data()
        old_users_list.append(new_user_data)

        with open(users_blend_path, 'w') as json_file:
            json.dump(old_users_list, json_file, indent=4)

        return jsonify(new_user_data), 201
    if(request.method == 'DELETE'):

        if not username:
            return jsonify({'message': 'It needs a username to delete. /users/<username>'}), 200

        old_users_list = load_users_data()

        find_user_by_username = next((user for user in old_users_list if user['username'] == username), None)

        if len(old_users_list) > 0 and find_user_by_username is not None:

            new_users_list = list(filter(lambda userObject: userObject['username'] != username, list(old_users_list)))

            with open(users_blend_path, 'w') as json_file:
                json.dump(new_users_list, json_file, indent=4)

            return jsonify({'message': 'User deleted with success'}), 200
        elif len(old_users_list) > 0 and find_user_by_username is None:
            return jsonify({'message': 'Doesn\'t exist users with this username'}), 200
  
        return jsonify({'message': 'There\'s no users to delete. Add a new user being able to delete'}), 200
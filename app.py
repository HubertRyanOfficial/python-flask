import json
from flask import Flask, jsonify
from configure_user_blend import load_users_data
from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix='/users')

@app.route('/')
def index():
    all_users = load_users_data()
    return jsonify({'message': 'Nice! You\'re using Oddity database.', 'total_users': len(all_users)})

if __name__ == "__main__":
    app.run(debug=True)
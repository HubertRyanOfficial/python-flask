import json
from flask import Flask, jsonify

from routes.user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes, url_prefix='/users')

@app.route('/')
def index():
    return jsonify({'message': 'Nice! You\'re using Oddity database.'})

if __name__ == "__main__":
    app.run(debug=True)
import os

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt_extended import JWTManager, create_access_token

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister

from hmac import compare_digest
from models.user import UserModel

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'rafael'
api = Api(app)

jwt = JWTManager(app)  # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({'message': 'Missing or invalid token.'}), 401


@app.route('/auth', methods=['POST'])
def auth():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({'message': 'Invalid credentials'}), 401

from db import init_db

init_db(app)


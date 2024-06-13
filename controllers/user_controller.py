from flask import Blueprint, request, jsonify
from shop.model.da.database import DatabaseManager
from shop.model.entity.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

user_blueprint = Blueprint('user', __name__)
db_manager = DatabaseManager()

SECRET_KEY = 'your_secret_key'

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400

    if db_manager.filter(User, username=username):
        return jsonify({'message': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db_manager.add(new_user)

    return jsonify({'message': 'User registered successfully'}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = db_manager.filter(User, username=username)

    if not user or not check_password_hash(user[0].password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    token = jwt.encode({'user_id': user[0].id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, SECRET_KEY)

    return jsonify({'token': token}), 200

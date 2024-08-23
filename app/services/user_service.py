from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt
from app import db, blacklist
from app.models import User

def register_user(data):
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing fields'}), 400

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'error': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

def login_user(data):
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing fields'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token), 200

def logout_user():
    jti = get_jwt()['jti']
    blacklist.add(jti)
    return jsonify({'message': 'Successfully logged out'}), 200

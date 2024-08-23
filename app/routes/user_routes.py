from flask import request
from flask_jwt_extended import jwt_required
from app import app
from app.services import user_service

@app.route('/register', methods=['POST'])
def register():
    return user_service.register_user(request.get_json())

@app.route('/login', methods=['POST'])
def login():
    return user_service.login_user(request.get_json())

@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    return user_service.logout_user()

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return jsonify({'message': f'Welcome {user.username}'})

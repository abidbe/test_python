from flask import request
from flask_jwt_extended import jwt_required
from app import app
from app.models import Data
from app.services import data_service

@app.route('/data', methods=['GET'])
@jwt_required()
def get_all_data():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return data_service.get_paginated_data(page, per_page)

@app.route('/data/filter', methods=['GET'])
@jwt_required()
def filter_data():
    name = request.args.get('name')
    age = request.args.get('age', type=int)
    return data_service.filter_data(name, age)

@app.route('/data', methods=['POST'])
@jwt_required()
def create_data():
    name = request.form.get('name')
    age = request.form.get('age')
    city = request.form.get('city')
    file = request.files.get('file')
    return data_service.create_new_data(name, age, city, file)

@app.route('/data/<int:id>', methods=['GET'])
@jwt_required()
def get_data(id):
    data = Data.query.get(id)
    if data is None:
        return jsonify({'message': 'Data not found'}), 404
    return data_service.data_schema.dump(data)

@app.route('/data/<int:id>', methods=['PUT'])
@jwt_required()
def update_data(id):
    data = Data.query.get(id)
    if data is None:
        return jsonify({'message': 'Data not found'}), 404
    return data_service.update_existing_data(data, request.json)

@app.route('/data/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_data(id):
    data = Data.query.get(id)
    if data is None:
        return jsonify({'message': 'Data not found'}), 404
    return data_service.delete_data_by_id(data)

@app.route('/uploads/<filename>', methods=['GET'])
def download_file(filename):
    return data_service.download_file(filename)

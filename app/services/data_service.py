import os
from flask import jsonify
from werkzeug.utils import secure_filename
from app import db, app
from app.models import Data
from app.schemas import data_schema, datas_schema
from app.utils import allowed_file

def get_paginated_data(page, per_page):
    data_paginated = Data.query.paginate(page=page, per_page=per_page, error_out=False)
    result = datas_schema.dump(data_paginated.items)
    return jsonify({
        'data': result,
        'total': data_paginated.total,
        'pages': data_paginated.pages,
        'current_page': data_paginated.page,
        'next_page': data_paginated.next_num,
        'prev_page': data_paginated.prev_num 
    })

def filter_data(name, age):
    query = Data.query
    if name:
        query = query.filter(Data.name.ilike(f'%{name}%'))
    if age:
        query = query.filter_by(age=age)
    
    filtered_data = query.all()
    result = datas_schema.dump(filtered_data)
    return jsonify(result)

def create_new_data(name, age, city, file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        new_data = Data(name=name, age=age, city=city, file_path=file_path)
        db.session.add(new_data)
        db.session.commit()
        
        return jsonify({
            'message': 'Data created and file uploaded successfully!',
            'data': data_schema.dump(new_data)
        }), 201
    else:
        return jsonify({'error':'File type not allowed'}), 400

def update_existing_data(data, updated_data):
    data.name = updated_data.get('name')
    data.age = updated_data.get('age')
    data.city = updated_data.get('city')
    db.session.commit()
    return jsonify({"message": "Data updated", "data": data_schema.dump(data)})

def delete_data_by_id(data):
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": "Data deleted", "data": data_schema.dump(data)})

def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

from app import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    file_path = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f"<Data {self.name}>"
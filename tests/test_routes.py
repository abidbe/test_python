import unittest
from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

        # Buat user test untuk login
        hashed_password = generate_password_hash('testpassword', method='sha256')
        user = User(username='testuser', email='testuser@example.com', password=hashed_password)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/register', json={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', response.get_data(as_text=True))

    def test_login(self):
        # Pastikan user test sudah ada di database sebelum login
        response = self.app.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)  # Perbaiki di sini untuk memeriksa kode 200
        self.assertIn('access_token', response.get_data(as_text=True))

if __name__ == "__main__":
    unittest.main()

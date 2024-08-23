import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-string')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:admin@localhost/test')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/uploads'))
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

# Opsi untuk menggunakan konfigurasi yang berbeda
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Untuk menggunakan konfigurasi, Anda bisa mengatur `app.config.from_object()` di __init__.py

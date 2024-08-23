from flask import jsonify
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not Found', 'message': 'The requested resource could not be found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()  # Rollback transaksi jika terjadi error
    return jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred on the server.'}), 500

# Anda juga bisa menambahkan handler untuk error lain seperti 403, 401, dsb.

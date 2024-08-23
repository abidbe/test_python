
# Flask Web Application

## Introduction
This is a web application built with [Flask](https://flask.palletsprojects.com/), a lightweight web framework for Python. The application includes user authentication, file uploads, and data management with a PostgreSQL database.

## Features
- User registration and login with JWT-based authentication
- File upload functionality with validation for allowed file types
- RESTful API endpoints for managing data (CRUD operations)
- Pagination and filtering of data
- Error handling and custom middleware
- Unit testing using `unittest`

## Project Structure
```
TEST2/
│
├── app/
│   ├── __init__.py            # Initialize Flask application and extensions
│   ├── config.py              # Configuration settings for the application
│   ├── models/                # Database models
│   │   ├── __init__.py
│   │   ├── data_model.py      # Data model definition
│   │   └── user_model.py      # User model definition
│   ├── routes/                # Application routes
│   │   ├── __init__.py
│   │   ├── data_routes.py     # Routes related to data operations
│   │   └── user_routes.py     # Routes related to user authentication
│   ├── services/              # Business logic and service layer
│   │   ├── __init__.py
│   │   ├── data_service.py    # Logic related to data operations
│   │   └── user_service.py    # Logic related to user operations
│   ├── schemas.py             # Marshmallow schemas for data serialization
│   ├── utils.py               # Utility functions
│   ├── static/                # Static files (uploads, etc.)
│   │   └── uploads/           # Directory for uploaded files
├── migrations/                # Database migrations
├── tests/                     # Unit tests
│   ├── __init__.py
│   └── test_routes.py         # Test cases for API routes
├── venv/                      # Virtual environment (not included in the repo)
├── app.py                     # Entry point of the application
├── requirements.txt           # Python dependencies
└── .gitignore                 # Git ignore file
```

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- Virtualenv (recommended)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/abidbe/test_python.git
    cd test_python
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**: Create a `.env` file in the root directory and add the following:

    ```plaintext
    SECRET_KEY=your-secret-key
    JWT_SECRET_KEY=your-jwt-secret-key
    DATABASE_URL=postgresql://username:password@localhost/your_database
    ```

5. **Initialize the database**:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. **Run the application**:

    ```bash
    python app.py
    ```

7. **Run tests**:

    ```bash
    python -m unittest discover tests
    ```

## Usage
Once the application is running, you can access the API endpoints via a tool like Postman or cURL.

- **Register a new user**:
  ```
  POST /register
  ```

- **Login**:
  ```
  POST /login
  ```

- **Get data**:
  ```
  GET /data
  ```

- **Upload data with a file**:
  ```
  POST /data
  ```

Refer to the individual routes for more details on how to use each endpoint.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Flask documentation: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Flask-JWT-Extended documentation: [https://flask-jwt-extended.readthedocs.io/](https://flask-jwt-extended.readthedocs.io/)
- Flask-SQLAlchemy documentation: [https://flask-sqlalchemy.palletsprojects.com/](https://flask-sqlalchemy.palletsprojects.com/)

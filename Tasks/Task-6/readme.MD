#  FastAPI Application

A FastAPI application implementing user registration and authentication using JWT tokens.

## Installation
1. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy alembic bcrypt pyjwt python-multipart

```

3. Run the application:
```bash 
uvicorn FastAPI.main:app --reload
```

## API Endpoints

### POST /register/
Register a new user.

**Request Body:**
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "id": 1,
  "username": "string",
  "email": "string"
}
```

### POST /login/
Authenticate user and return JWT token.

**Request Body:**
```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```



## Authentication
- Passwords are hashed using bcrypt
- JWT tokens are used for authentication with 30-minute expiration
- Tokens are passed in the Authorization header as Bearer tokens



# Flask TODO API

A production-ready Flask API for managing TODO items with full CRUD operations.

## Features

- RESTful API with JSON responses
- SQLite database with SQLAlchemy ORM
- Data validation with Marshmallow
- Comprehensive error handling
- Unit tests with pytest
- Virtual environment support

## Structure

- `app/` - application package
  - `__init__.py` - app factory
  - `config.py` - configuration
  - `models.py` - database models
  - `routes.py` - API endpoints
  - `schemas.py` - serialization schemas
- `tests/` - unit tests
- `run.py` - application entrypoint
- `requirements.txt` - dependencies

## API Endpoints

### GET /
Health check endpoint.

### GET /todos
Retrieve all TODO items.

### GET /todos/{id}
Retrieve a specific TODO item by ID.

### POST /todos
Create a new TODO item.

**Request Body:**
```json
{
  "title": "Buy groceries",
  "description": "Milk, bread, eggs",
  "completed": false
}
```

### PUT /todos/{id}
Update an existing TODO item.

**Request Body:** (partial update supported)
```json
{
  "title": "Buy groceries and fruits",
  "completed": true
}
```

### DELETE /todos/{id}
Delete a TODO item.

## Run

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py

# Run tests
pytest
```

## Environment Variables

- `SECRET_KEY`: Flask secret key (default: "change-me")
- `FLASK_DEBUG`: Enable debug mode (default: "1")
- `DATABASE_URL`: Database URI (default: "sqlite:///todo.db")
# todo-flask-api

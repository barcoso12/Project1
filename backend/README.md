# FastAPI Starter Project

This is a starter project for FastAPI with a basic structure.

## Structure
- `app/`: Contains the application code.
- `models.py`: SQLAlchemy models.
- `routers.py`: API routes.
- `crud.py`: CRUD operations.
- `db.py`: Database connection.
- `schemas.py`: Pydantic schemas for validation.
- `requirements.txt`: Python dependencies.

## Getting Started
1. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints
- `/items/`: Create a new item

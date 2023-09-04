# PythonFastApiProjectByMe
Python fastAPI project with SQLAlchemy and Alembic migrations
Project was created with:

poetry new PythonFastApiProjectByMe

poetry add fastapi sqlalchemy alembic uvicorn

### Create Install dependencies
poetry install

### Create database
uvicorn app.main:app --reload
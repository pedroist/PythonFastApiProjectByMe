# PythonFastApiProjectByMe
Python fastAPI project with SQLAlchemy and Alembic migrations
Project was created with:

```sh
poetry new PythonFastApiProjectByMe

poetry add fastapi sqlalchemy alembic uvicorn
```

### Create Install dependencies
```sh
poetry install
```

### Create database
```sh
uvicorn app.main:app --reload
```

### Write queries in sqlite
**Note:** sqlite comes by default with home brew:

```sh
brew list
```

```sh
sqlite3 app/todosapp.db

.schema (returns schema of todos.db)

select * from todos;

insert into todos (title, description, priority, complete) values ('Go to the store', 'Pick up eggs', 5, False); 

update todos set priority = 4 where id = 1;

delete from todos where id = 1;
```
**Note:** Queries need semicolon at the end

To change the display mode:
```sh
.mode table
.mode box
```

###Generate Secret key:
On the terminal:

```sh
openssl rand -hex 32
```

###Using MySQL:
 Had to install with pip:

 ```sh
pip install pymysql
```

###Alembic:
```sh
alembic init alembic
```
It creates a folder called 'alembic'

Then we need to config alembic (files alembic.ini and alembic/env.py)

Then, create the revision:

```sh
alembic revision -m "create phone number for user col"
```

Then after changing the revision file, apply the changes to the database by running:

```sh
alembic upgrade <revision_number>
```
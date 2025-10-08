[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.105-green)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-orange)](https://www.sqlite.org/index.html)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

# FastAPI User Management System

This project creates a simple user management system using **FastAPI**, **SQLite**, and **Jinja2**. Users can register with the system, log in, and view their passwords if they forget them.

---

## Features 🌟

- User Registration
- User Login  
- View Dashboard
- Forgotten Password 
- Store user data with SQLite database 
- HTML templating with Jinja2

---

## Installation 💻

### 1. Clone the project:
```bash
git clone https://github.com/ArdaAlp/API-Login-Tutorial.git
cd "API-Login-Tutorial"
```

<br>

### 2. Create and activate a virtual environment:
```python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

<br>

### 3. Install the required packages:
```
pip install fastapi uvicorn jinja2 pydantic
```

---

## Usage 📌
- #### Register: Register with a username and password on the ```/register``` page.

- #### Login: Log in with your username and password on the ```/login``` page.

- #### Forgotten Password: You can view your password by entering your username on the ```/forgotten``` page.

- #### Dashboard: After a successful login, the dashboard where you can view all user data will open.

---

## Running ▶️
*From Console:* ```uvicorn main:app --reload``` **or** ```fastapi dev app.py```

*From Browser:* ```http://127.0.0.1:8000```

*Swagger:* ```http://127.0.0.1:8000/docs```

---

## Database 🗂
*The database uses SQLite and is stored as* ```users.db``` *in the project directory.*

The ```user``` table has the following fields:

| Field     | Type     | Description              |
| -------- | ------- | ----------------------     |
| id       | INTEGER | Auto-incrementing ID       |
| username | TEXT    | Username (unique)          |
| password | TEXT    | Password                   |

---

## Notes 🔧
- *This project is for prototyping purposes, and passwords are stored as plain text. Hashing should be used in a production environment.*

- ***To enhance the project**, you could add user roles, token-based authentication, or integrate a frontend framework.*

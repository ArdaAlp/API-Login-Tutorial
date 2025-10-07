import sqlite3
from pydantic import BaseModel
from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


def get_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL
                   )
                ''')
    conn.commit()
    conn.close()


get_db()


def User(BaseModel):
    username: str
    password: str

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register(request: Request, username: str = Form(...), password: str = Form(...)):

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)", (username, password))

    conn.commit()
    conn.close()
    
    return RedirectResponse(url="/login", status_code=303)

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    data = [dict(zip(columns, rows)) for rows in rows]


    conn.close()

    if user:
        return templates.TemplateResponse("dashboard.html", {"request": request, "user": user, "data": data})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Kullanıcı Adı veya Şifre Hatalı."})
    
@app.get("/forgotten")
def forgotten_page(request: Request):
    return templates.TemplateResponse("forgotten.html", {"request": request})

@app.post("/forgotten")
def forgotten(request: Request, username: str = Form(...)):

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM user WHERE username = ?", (username,))
    users = cursor.fetchone()

    conn.close()
    
    if users:
        username = users[1]
        password = users[2]
        return templates.TemplateResponse("forgotten.html", {"request": request, "password": password, "username": username})
    else:   
        return templates.TemplateResponse("forgotten.html", {"request": request, "error": "Kullanıcı bulunamadı."})
    

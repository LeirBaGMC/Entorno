from fastapi import FastAPI, Query
from sqlmodel import SQLModel

app = FastAPI(title="API REST mínima con SQLModel")

# --- Modelo ---
class User(SQLModel):
    id: int
    username: str
    password: str
    is_active: bool = True


usuarios = [
    User(id=1, username="alice", password="123", is_active=True),
    User(id=2, username="bob", password="123", is_active=True),
]
next_id = 3

# --- Endpoints ---
@app.get("/")
def read_root():
    return {"mensaje": "Hola, FastAPI funciona..."}

@app.post("/login")
def login(username: str = Query(...), password: str = Query(...)):
    for u in usuarios:  # misma lógica que antes
        if u.username == username and u.password == password:
            return {"ok": True, "msg": f"Bienvenido {username}"}
    return {"ok": False, "msg": "Usuario o contraseña inválidos"}

@app.get("/users")
def list_users():
    return usuarios

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in usuarios:
        if u.id == user_id:
            return u

@app.post("/users")
def create_user(username: str = Query(...), password: str = Query(...)):
    global next_id
    user = User(id=next_id, username=username, password=password, is_active=True)
    usuarios.append(user)
    next_id += 1
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str = Query(None), is_active: bool = Query(None)):
    for u in usuarios:
        if u.id == user_id:
            if username:
                u.username = username
            if is_active is not None:
                u.is_active = is_active
            return u

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for u in usuarios:
        if u.id == user_id:
            usuarios.remove(u)
            return {"msg": "Usuario eliminado"}

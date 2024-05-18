# Link para o tutorial: https://kinsta.com/pt/blog/fastapi/
# Link para a documentação interativa automatica: http://localhost:8000/docs#/

from typing import List
from uuid import uuid4
from fastapi import FastAPI
from model import Gender, Role, UpdateUser, User
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()

# O codigo abaixo é um exemplo de como você pode criar um banco de dados falso. db é uma lista de usuários no qual cada usuário é uma instância da classe User. Os usuários são criados com uuid4() e os valores dos atributos são definidos manualmente. db é um tipo de lista de usuários simulando um banco de dados in-memory.
db: List[User] = [
 User(
 id=uuid4(),
 first_name="John",
 last_name="Doe",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Jane",
 last_name="Doe",
 gender=Gender.female,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="James",
 last_name="Gabriel",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Eunit",
 last_name="Eunit",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),
]

@app.get("/")
async def root():
 return {"Hello": "World",}

# O código abaixo é um exemplo de como você pode criar uma rota para ler todos os usuários do banco de dados in-memory. A rota é definida com o decorador app.get() e o caminho da rota é "/api/v1/users". A função get_users() retorna o banco de dados falso db.
@app.get("/api/v1/users")
async def get_users():
    return db

# O codigo abaixo é um exemplo de como você pode criar uma rota para criar um novo usuário no banco de dados in-memory. A rota é definida com o decorador app.post() e o caminho da rota é "/api/v1/users". A função create_user() recebe um objeto do tipo User e adiciona o usuário ao banco de dados falso db. A função retorna o id do usuário criado.
@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

# O código abaixo é um exemplo de como você pode criar uma rota para ler um usuário específico do banco de dados in-memory. A rota é definida com o decorador app.get() e o caminho da rota é "/api/v1/users/{user_id}". A função get_user() recebe um id de usuário e retorna o usuário correspondente do banco de dados falso db.
@app.delete("/api/v1/users/{user_id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail=f"Delete user failed, id {id} not found.")

# O código abaixo é um exemplo de como você pode criar uma rota para atualizar um usuário no banco de dados in-memory. A rota é definida com o decorador app.put() e o caminho da rota é "/api/v1/users/{user_id}". A função update_user() recebe um id de usuário e um objeto do tipo UpdateUser. A função procura o usuário correspondente no banco de dados falso db e atualiza os atributos do usuário com os valores fornecidos no objeto UpdateUser. A função retorna o id do usuário atualizado.
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, id: UUID):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
    raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")
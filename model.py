from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    # uuid4() é uma função que gera um UUID (id) aleatório e único. 
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender:  Gender
    roles: List[Role]

# O código abaixo é um exemplo de como você pode criar um modelo de atualização de usuário. O modelo UpdateUser é uma subclasse de BaseModel. O modelo UpdateUser tem os mesmos atributos que o modelo User, mas todos os atributos são opcionais. Isso significa que você pode atualizar um ou mais atributos de um usuário sem precisar fornecer todos os atributos.
class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]
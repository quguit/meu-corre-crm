from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    cpf: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    id: int
    data_cadastro: datetime

class config:
    orm_mode=True
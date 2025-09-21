from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ---------------------------------------------------------
# Base: atributos comuns entre criação e resposta
# ---------------------------------------------------------
class ClienteBase(BaseModel):
    nome: str
    telefone: str
    email: EmailStr
    cpf: Optional[str] = None

# ---------------------------------------------------------
# Schema para criação de cliente (todos obrigatórios)
# ---------------------------------------------------------
class ClienteCreate(ClienteBase):
    """
    Schema usado na criação de novos clientes.
    """
    pass

# ---------------------------------------------------------
# Schema para atualização de cliente (todos opcionais)
# ---------------------------------------------------------
class ClienteUpdate(BaseModel):
    """
    Schema usado para atualização parcial de clientes.
    Todos os campos são opcionais.
    """
    nome: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None

    class Config:
        orm_mode = True

# ---------------------------------------------------------
# Schema de resposta: inclui campos gerados pelo banco
# ---------------------------------------------------------
class Cliente(ClienteBase):
    """
    Schema usado nas respostas da API.
    Inclui os campos gerados automaticamente.
    """
    id: int
    data_cadastro: datetime

    class Config:
        orm_mode = True

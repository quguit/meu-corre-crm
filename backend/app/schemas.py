from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# =====================================================
# CLIENTE
# =====================================================
class ClienteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    tipo: Optional[str] = None  # ex.: "logista", "comprador", "prospecção"

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    tipo: Optional[str] = None

class ClienteOut(ClienteBase):
    id: int
    data_cadastro: datetime

    class Config:
        orm_mode = True


# =====================================================
# VEÍCULO
# =====================================================
class VeiculoBase(BaseModel):
    marca: str
    modelo: str
    ano: int
    preco: float
    status: str  # ex.: "disponível", "vendido", "em negociação"

class VeiculoCreate(VeiculoBase):
    pass

class VeiculoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano: Optional[int] = None
    preco: Optional[float] = None
    status: Optional[str] = None

class VeiculoOut(VeiculoBase):
    id: int

    class Config:
        orm_mode = True


# =====================================================
# VENDA
# =====================================================
class VendaBase(BaseModel):
    cliente_id: int
    veiculo_id: int
    valor_final: float
    forma_pagamento: str  # ex.: "à vista", "financiado", "parcelado"

class VendaCreate(VendaBase):
    pass

class VendaUpdate(BaseModel):
    valor_final: Optional[float] = None
    forma_pagamento: Optional[str] = None

class VendaOut(VendaBase):
    id: int
    data_venda: datetime

    cliente: Optional[ClienteOut]
    veiculo: Optional[VeiculoOut]

    class Config:
        orm_mode = True


# =====================================================
# INTERAÇÃO (ex.: ligação, WhatsApp, email)
# =====================================================
class InteracaoBase(BaseModel):
    cliente_id: int
    tipo: str  # "ligação", "mensagem", "email"
    descricao: Optional[str] = None

class InteracaoCreate(InteracaoBase):
    pass

class InteracaoOut(InteracaoBase):
    id: int
    data_interacao: datetime

    class Config:
        orm_mode = True

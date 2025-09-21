from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"  # Nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True, nullable=False)
    telefone = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    cpf = Column(String, unique=True, index=True, nullable=False)
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())

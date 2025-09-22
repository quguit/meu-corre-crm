from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text, Enum, func
from sqlalchemy.orm import relationship
from .database import Base
import enum

# ==============================
# ENUMS AUXILIARES
# ==============================
class ClienteStatus(str, enum.Enum):
    NOVO = "novo"
    EM_NEGOCIACAO = "em_negociacao"
    ATIVO = "ativo"
    INATIVO = "inativo"
    FIDELIZADO = "fidelizado"


class FormaPagamento(str, enum.Enum):
    AVISTA = "avista"
    PARCELADO = "parcelado"
    FINANCIAMENTO = "financiamento"
    CONSIGNADO = "consignado"


class TipoContato(str, enum.Enum):
    LIGACAO = "ligacao"
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    PRESENCIAL = "presencial"


# ==============================
# USUÁRIO / VENDEDOR
# ==============================
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hash = Column(String, nullable=False)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    vendas = relationship("Venda", back_populates="vendedor")
    contatos = relationship("Contato", back_populates="usuario")


# ==============================
# CLIENTE
# ==============================
class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    telefone = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    cpf = Column(String, unique=True, index=True, nullable=True)
    status = Column(Enum(ClienteStatus), default=ClienteStatus.NOVO)
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    vendas = relationship("Venda", back_populates="cliente")
    contatos = relationship("Contato", back_populates="cliente")


# ==============================
# VEÍCULO
# ==============================
class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    cor = Column(String, nullable=True)
    placa = Column(String, unique=True, index=True, nullable=True)
    chassi = Column(String, unique=True, index=True, nullable=True)
    preco = Column(Float, nullable=False)
    status = Column(String, default="disponivel")  # disponivel, reservado, vendido
    data_cadastro = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    vendas = relationship("Venda", back_populates="veiculo")


# ==============================
# VENDA
# ==============================
class Venda(Base):
    __tablename__ = "vendas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    veiculo_id = Column(Integer, ForeignKey("veiculos.id"))
    vendedor_id = Column(Integer, ForeignKey("usuarios.id"))

    forma_pagamento = Column(Enum(FormaPagamento), nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, default="em_negociacao")  # em_negociacao, concluida, cancelada

    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_fechamento = Column(DateTime(timezone=True), nullable=True)

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="vendas")
    veiculo = relationship("Veiculo", back_populates="vendas")
    vendedor = relationship("Usuario", back_populates="vendas")


# ==============================
# CONTATO / FOLLOW-UP
# ==============================
class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    tipo = Column(Enum(TipoContato), nullable=False)
    resumo = Column(Text, nullable=True)
    proxima_acao = Column(DateTime(timezone=True), nullable=True)

    data_contato = Column(DateTime(timezone=True), server_default=func.now())

    # Relacionamentos
    cliente = relationship("Cliente", back_populates="contatos")
    usuario = relationship("Usuario", back_populates="contatos")

from sqlalchemy.orm import Session
from . import models, schemas

def get_clientes(db: Session, skip: int = 0, int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def get_cliente_by_email(db: Session, email:str):
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email,
        cpf=cliente.cpf
    )
    db.add(db_cliente) #adiciona à sessão
    db.commit() #comita a transação para salvar no banco
    db.refresh(db_cliente)  #atualiza o objeto com o id gerado pelo banco
    return db_cliente
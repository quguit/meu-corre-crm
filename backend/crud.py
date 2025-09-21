from sqlalchemy.orm import Session
from . import models, schemas

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    """Retorna todos os clientes, com paginação"""
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def get_cliente_by_email(db: Session, email: str):
    """Busca um cliente pelo e-mail"""
    return db.query(models.Cliente).filter(models.Cliente.email == email).first()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    """Cria um novo cliente"""
    db_cliente = models.Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email,
        cpf=cliente.cpf
    )
    db.add(db_cliente)  # adiciona à sessão
    db.commit()  # comita a transação para salvar no banco
    db.refresh(db_cliente)  # atualiza o objeto com o id gerado pelo banco
    return db_cliente

def get_cliente(db: Session, cliente_id: int):
    """Retorna um cliente pelo ID"""
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteUpdate):
    """Atualiza um cliente existente"""
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return None
    
    # Pega os dados do schema de atualização
    update_data = cliente.dict(exclude_unset=True)

    # Atualiza os campos no objeto do banco
    for key, value in update_data.items():
        setattr(db_cliente, key, value)

    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    """Deleta um cliente pelo ID"""
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return None
    db.delete(db_cliente)
    db.commit()
    return db_cliente

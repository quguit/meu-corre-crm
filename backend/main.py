from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import SessionLocal, engine

# Cria as tabelas no banco (se não existirem)
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Meu Corre | Vendas na Mão",
    version="0.1.0"
)

# Função para obter uma sessão do banco de dados para cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clientes/", response_model=schemas.Cliente, status_code=201)
def create_new_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    """
    Cria um novo cliente.
    """
    db_cliente = crud.get_cliente_by_email(db, email=cliente.email)
    if db_cliente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    return crud.create_cliente(db=db, cliente=cliente)


@app.get("/clientes/", response_model=List[schemas.Cliente])
def read_all_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retorna uma lista com todos os clientes.
    """
    clientes = crud.get_clientes(db, skip=skip, limit=limit)
    return clientes

@app.get("/")
def read_root():
    return {"status": "API 'Meu Corre' no ar!", "ambiente": "Docker"}
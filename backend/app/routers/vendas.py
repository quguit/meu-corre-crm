from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/vendas",
    tags=["Vendas"]
)

# Criar venda
@router.post("/", response_model=schemas.VendaOut, status_code=201)
def create_venda(venda: schemas.VendaCreate, db: Session = Depends(get_db)):
    # Verifica se o cliente existe
    cliente = db.query(models.Cliente).filter(models.Cliente.id == venda.cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    # Verifica se o veículo existe
    veiculo = db.query(models.Veiculo).filter(models.Veiculo.id == venda.veiculo_id).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    nova_venda = models.Venda(**venda.dict())
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    return nova_venda


# Listar todas as vendas
@router.get("/", response_model=List[schemas.VendaOut])
def get_vendas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Venda).offset(skip).limit(limit).all()


# Buscar venda por ID
@router.get("/{venda_id}", response_model=schemas.VendaOut)
def get_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = db.query(models.Venda).filter(models.Venda.id == venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")
    return venda


# Atualizar venda
@router.put("/{venda_id}", response_model=schemas.VendaOut)
def update_venda(venda_id: int, update: schemas.VendaUpdate, db: Session = Depends(get_db)):
    venda = db.query(models.Venda).filter(models.Venda.id == venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    for field, value in update.dict(exclude_unset=True).items():
        setattr(venda, field, value)

    db.commit()
    db.refresh(venda)
    return venda


# Deletar venda
@router.delete("/{venda_id}", response_model=schemas.VendaOut)
def delete_venda(venda_id: int, db: Session = Depends(get_db)):
    venda = db.query(models.Venda).filter(models.Venda.id == venda_id).first()
    if not venda:
        raise HTTPException(status_code=404, detail="Venda não encontrada")

    db.delete(venda)
    db.commit()
    return venda

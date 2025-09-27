from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/veiculos",
    tags=["Veículos"]
)

# Criar veículo
@router.post("/", response_model=schemas.VeiculoOut, status_code=201)
def create_veiculo(veiculo: schemas.VeiculoCreate, db: Session = Depends(get_db)):
    novo_veiculo = models.Veiculo(**veiculo.dict())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo


# Listar todos os veículos
@router.get("/", response_model=List[schemas.VeiculoOut])
def get_veiculos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Veiculo).offset(skip).limit(limit).all()


# Buscar veículo por ID
@router.get("/{veiculo_id}", response_model=schemas.VeiculoOut)
def get_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(models.Veiculo).filter(models.Veiculo.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo


# Atualizar veículo
@router.put("/{veiculo_id}", response_model=schemas.VeiculoOut)
def update_veiculo(veiculo_id: int, update: schemas.VeiculoUpdate, db: Session = Depends(get_db)):
    veiculo = db.query(models.Veiculo).filter(models.Veiculo.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    for field, value in update.dict(exclude_unset=True).items():
        setattr(veiculo, field, value)

    db.commit()
    db.refresh(veiculo)
    return veiculo


# Deletar veículo
@router.delete("/{veiculo_id}", response_model=schemas.VeiculoOut)
def delete_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(models.Veiculo).filter(models.Veiculo.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    db.delete(veiculo)
    db.commit()
    return veiculo

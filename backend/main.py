from fastapi import FastAPI
from . import models  # Importa os modelos
from .database import engine # Importa a engine

# Este comando instrui o SQLAlchemy a criar todas as tabelas no banco
# com base nos modelos que definimos
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Meu Corre | Vendas na Mão",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "API 'Meu Corre' no ar!", "ambiente": "Docker"}

# Aqui vamos adicionar o endpoint para criar clientes no próximo passo!
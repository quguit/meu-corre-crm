from fastapi import FastAPI

app = FastAPI(
    title="Meu Corre | Vendas na Mão",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"status": "API 'Meu Corre' começou!", "ambiente": "Docker"}
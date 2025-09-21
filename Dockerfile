# 1. Imagem base
FROM python:3.11-slim

# 2. Diretório de trabalho
WORKDIR /app

# 3. Copia as dependências
COPY backend/requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia o código da API
COPY ./backend .

# 6. Expõe a porta do FastAPI
EXPOSE 8010

# 7. Comando de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8010", "--reload"]


# 1. Imagem base
FROM python:3.11-slim

# 2. Diretório de trabalho dentro do container
WORKDIR /app

# 3. Copia o arquivo de dependências para o container
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o código do backend para dentro do contêiner
COPY ./backend .

# 6. Expõe a porta que o FastAPI usará
EXPOSE 0801

# 7. Comando para iniciar a API quando execultar o container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "0801", "--reload"]
# --host 0.0.0.0 faz com que o servidor escute em todas as interfaces de rede,
# Crucial para docker conseguir expor a porta
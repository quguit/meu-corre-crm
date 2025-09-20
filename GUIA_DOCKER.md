C
# Guia de Docker & Docker Compose para Projetos Python

Este guia é um resumo prático de como estruturamos o ambiente do projeto **"Meu Corre"** e uma referência dos comandos essenciais para o dia a dia do desenvolvimento.

## 1\. A Arquitetura do Nosso Ambiente Docker

Para criar nosso ambiente isolado, utilizamos dois arquivos principais que trabalham juntos.

### 📜 `Dockerfile` - A Receita do Bolo

Este arquivo contém o passo a passo para construir a **imagem** da nossa aplicação (`api`). Uma imagem é um pacote que contém tudo que a aplicação precisa para rodar:

  - O sistema operacional base (Python 3.11-slim).
  - As dependências de sistema (se houver).
  - As bibliotecas Python (listadas no `requirements.txt`).
  - O nosso código-fonte.

### orche `docker-compose.yml` - O Maestro da Orquestra

Este arquivo descreve e conecta todos os **serviços** que compõem nosso projeto. Um serviço é uma instância em execução de uma imagem (um contêiner).

  - **`api`**: Nosso serviço de backend, construído a partir do `Dockerfile`.
  - **`db`**: Nosso serviço de banco de dados, que utiliza uma imagem pronta e oficial do PostgreSQL.

Ele também gerencia as **redes** (para que a `api` possa conversar com o `db`) e os **volumes** (para que os dados do banco de dados não se percam quando desligamos os contêineres).

-----

## 2\. 🚀 Comandos Essenciais do Dia a Dia

Estes são os comandos que você mais usará. **Lembre-se: sempre execute-os a partir da pasta raiz do projeto**, onde o arquivo `docker-compose.yml` está localizado.

### Iniciar e Parar o Ambiente

  * **Subir o ambiente (e ver os logs):**

    ```bash
    docker-compose up
    ```

    Este comando lê o `docker-compose.yml`, cria e inicia os contêineres. O terminal ficará "preso" mostrando os logs em tempo real de todos os serviços.

  * **Subir o ambiente e RECONSTRUIR a imagem:**

    ```bash
    docker-compose up --build
    ```

    **Use este comando sempre que você alterar o `Dockerfile` ou o `requirements.txt`**. A flag `--build` força a reconstrução da sua imagem `api` antes de iniciar.

  * **Subir o ambiente em segundo plano (detached mode):**

    ```bash
    docker-compose up -d
    ```

    A flag `-d` libera seu terminal após iniciar os contêineres. É o modo mais comum para trabalhar no dia a dia.

  * **Parar e REMOVER os contêineres:**

    ```bash
    docker-compose down
    ```

    Este é o desligamento completo. Ele para e remove os contêineres e a rede criada. É ótimo para garantir um ambiente limpo antes de subir novamente.

  * **Apenas parar os contêineres (pausar):**

    ```bash
    docker-compose stop
    ```

    Isso apenas "pausa" os contêineres. Você pode iniciá-los novamente com `docker-compose start`.

### 🔍 Verificando o Status e Logs

  * **Ver o status dos seus serviços:**

    ```bash
    docker-compose ps
    ```

    Mostra quais contêineres estão rodando (`Up`) ou parados (`Exited`).

  * **Ver os logs (se estiver rodando em detached mode):**

    ```bash
    docker-compose logs
    ```

    Mostra os logs de todos os serviços desde o início.

  * **Ver os logs de um serviço específico e "segui-los" em tempo real:**

    ```bash
    docker-compose logs -f api
    ```

    A flag `-f` (follow) é extremamente útil para depurar. Ela mostra os logs do serviço `api` em tempo real.

### 💻 Executando Comandos Dentro de um Contêiner

Esta é uma das funcionalidades mais poderosas para depuração.

  * **Abrir um terminal interativo (bash) dentro do contêiner da API:**

    ```bash
    docker-compose exec api bash
    ```

    Isso te dá acesso direto ao sistema de arquivos do contêiner. Você pode rodar `ls`, `pip freeze`, etc., para investigar o que está acontecendo lá dentro.

  * **Acessar o cliente de linha de comando do PostgreSQL:**

    ```bash
    docker-compose exec db psql -U user -d meudb
    ```

    Isso te conecta diretamente ao banco de dados `meudb` com o `user`. Útil para fazer consultas SQL rápidas.

### 🧹 Gerenciamento e Limpeza do Docker

Com o tempo, o Docker pode acumular muitas imagens e contêineres antigos, ocupando espaço em disco.

  * **Listar todas as imagens Docker no seu computador:**

    ```bash
    docker image ls
    ```

  * **Listar todos os contêineres (inclusive os parados):**

    ```bash
    docker container ls -a
    ```

  * **O "Faxinão" do Docker:**

    ```bash
    docker system prune -a --volumes
    ```

    **ATENÇÂO\!** Este comando remove **TUDO** que não está em uso no momento: todos os contêineres parados, todas as redes, todas as imagens "penduradas" e **todos os volumes**. É ótimo para liberar espaço, mas necessita de cautela.
## Backend Python Challenge

Desenvolva uma API REST que consuma um serviço [(JSON placeholder)](https://jsonplaceholder.typicode.com/todos) e retorne uma lista com os 5 primeiros resultados.

Ferramentas:

-   [requirements.txt](https://github.com/juliax5/flask-JSON-apirest/blob/main/requirements.txt)

Como executar:

```sh
git clone https://github.com/juliax5/flask-JSON-apirest.git
cd flask-JSON-apirest
python3 -m venv .venv
```

Ativando o ambiente virtual (Windows):

```sh
.venv/Scripts/activate  # (pwsh)
```

Ativando o ambiente virtual (Linux):

```sh
source .venv/bin/activate  # (bash)
```

Por fim:

```sh
pip install -r requirements.txt
flask run
```

Para acessar a API:

-   http://localhost:5000/

Para acessar o painel Swagger e testar os endpoints:

-   http://localhost:5000/apidoc/swagger

(Docker) Para criar a imagem:

```sh
docker build -t flaskinho .
```

Iniciar o container:

```sh
docker run -d -p 5000:5000 flaskinho
```

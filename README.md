# Django API com cache utilizando Redis

## Requisitos do projeto
- Ter docker instalado e configurado
- Usar ambiente linux para executar as macros


## Rodando o projeto
- Crie um arquivo ".env" e nele coloque as variaveis de ambiente conforme arquivo de exemplo.

- Use o seguinte comando para startar os containers:
``docker-compose up -d --build ``

- Rode as migrations:
`` make migrate ``

- Popule o banco de dados:
`` make populate ``

- Acesse pela URL: **http://localhost:8000/api/v1/product/**
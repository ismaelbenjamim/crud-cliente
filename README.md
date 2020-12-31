# CRUD de clientes
Repositório criado para uma aplicação com o framework Django que realiza o CRUD (Create, Read, Update, Delete) de clientes. Na realização dos testes do projeto foi usado o VENV e infelizmente ainda não foi feito o deploy da aplicação (será feito em breve).

<h2> 💻 Configuração para Desenvolvimento</h2>

1. Instale o Python:

<https://www.python.org/downloads/>

2. Instale o Virtualenv:
```
python -m venv myvenv
```

3. Instale as dependências do projeto:

```
Pip install -r requirements.txt
```

4. Realize as migrações para se banco de dados:
```
Python manage.py migrate
```

5. Para criar um super usuário no banco de dados:
```
Python manage.py createsuperuser
```

6. Inicie o projeto:
```
Python manage.py runserver
```

# Api Rest Controle Contas
## Descrição
Projeto de contas virtuais onde você pode creditar e debitar em uma conta e verificar o extrato da mesma

Projeto desenvolvido em Django e DjangoRestFramework.
```
(Servidor) => http://localhost:8011
```

## Rotas
```
admin/
contas/
contas/<numero_conta>
contas/<numero_conta>/extrato
contas/<numero_conta>/extrato_conta
contas/<numero_conta>/extrato_debito
debitar_creditar/
```


## Clonar o projeto
```
git clone https://github.com/morfimgabriel/controle-contas-rest-api.git
```

## Construir o projeto
A construção do projeto é feita com Docker sendo orquestrada por Docker-Compose
```
$ docker-compose up --build
$ docker-compose exec web python manage.py migrate
$ make test
```

## Stack
```
Python: 3.6
Django: 3.1.5
Django Rest Framework: 3.12.2
```

## Dependências Python3.6
```
asgiref==3.3.1
Django==3.1.5
djangorestframework==3.12.2
packaging==20.8
psycopg2-binary==2.8.6
pytz==2020.5
sqlparse==0.4.1
pyparsing==2.4.7
pytest==6.2.1
pytest-cov==2.11.1
pytest-django==4.1.0
python-dateutil==2.8.1
coverage==5.3.1
```


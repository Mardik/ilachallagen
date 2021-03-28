# Teste de Dev Trainee - Iago & Lubien & Associates

# Instuções sobre inicialização do ambinete de desenvolvimento

## Criar um ambiente de desenvolvimento Django com Docker

Com o git instalado e devidamente configurado rodar:

```console
git clone https://gitlab.com/devopspbs/django-docker-compose.git
cd django-docker-compose
```

Com docker e docker-compose devidamente instalados e configurados. Criar um novo projeto:

```console
docker-compose run web django-admin startproject devopspbsproject .
```

Se você estiver rodando Docker diretamente sobre Linux é necessário ajustar as permissões. Lembre-se de repetir o comando abaixo sempre que estiver problemas para acessar os arquivos diretamente no Docker host.

```console
sudo chown -R $USER:$USER .
```

Conectar o banco de dados:

1. No diretório do projeto edite o arquivo de configurações do Django, no nosso exemplo, o `devopspbsproject/settins.py`.

2. Substitua a sessão `DATABASES = ...` por:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

Por fim basta rodar `docker-compose up` para o Django ficar acessível em http://localhost:8000 .

Para rodar comandos no "container do Django" use `docker-compose exec web`, como por exemplo:

```console
docker-compose exec web django-admin help
```

## Referências

https://git-scm.com/downloads

https://docs.docker.com/install/

https://docs.docker.com/compose/install/

https://docs.docker.com/compose/django/

## License

GPLv3 or later.

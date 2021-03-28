# Teste de Dev Trainee - Iago & Lubien & Associates

## Instuções sobre inicialização do ambinete de desenvolvimento

Com o git instalado e devidamente configurado rodar:

```console
git clone https://github.com/Mardik/ilachallagen.git
cd ilachallagen
```

Com docker e docker-compose devidamente instalados e configurados. Executar o comando criação do banco de dados inicial:

```console
docker-compose run web python manage.py migrate
```

Se você estiver rodando Docker diretamente sobre Linux é pode ser necessário ajustar as permissões. Lembre-se de repetir o comando abaixo sempre que estiver problemas para acessar os arquivos diretamente no Docker host.

```console
sudo chown -R $USER:$USER .
```

Em seguinda inicie o container da aplicação:

```console
docker-compose up
```

## Referências

https://git-scm.com/downloads

https://docs.docker.com/install/

https://docs.docker.com/compose/install/

https://docs.docker.com/compose/django/

## License

GPLv3 or later.

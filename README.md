# E8

Необходимо установить docker и docker-compose.
Собрать образы командой
```
    docker-compose build
```
Их запустить с помощью команды 
```
    docker-compose up
```
Открыть ссылку
```
    http://0.0.0.0:5000/ 
```
Должно заработать))))  
```
alembic revision --autogenerate -m "initial migration"
alembic upgrade head

celery -A _celery worker --loglevel=info
```
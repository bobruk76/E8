# E8

1. Необходимо установить docker и docker-compose.
2. Собрать образы командой
    docker-compose build
3. Их запустить с помощью команды 
    docker-compose up
4. Открыть ссылку
    http://0.0.0.0:5000/ 
5. Должно заработать))))  

docker run --rm  --name flask-db -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres:12-alpine 

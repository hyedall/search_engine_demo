https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage

code/
|-- app/
|   |-- main.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
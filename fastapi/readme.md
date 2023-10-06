https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

docker build -t myimage .
docker run -d --name mycontainer -p 80:80 myimage

code/
|-- app/
|   |-- main.py
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt

uvicorn app.main:app --reload

git add fastapi/ && git commit -m "[update] # 3 page sucess - save" && git push origin main


1. 엘라스틱 - fastapi 연결




# query: str = Query(
    #     None, encoding="euc-kr", min_length=1
    # ),  # 기본값을 None으로 설정하여 옵셔널로 만듦
):
    # async def read_item(item_id: str, q: Optional[str] = None):
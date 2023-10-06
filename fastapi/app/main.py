from fastapi import FastAPI, Form, Request, Depends, HTTPException, Query
from typing import Optional
from fastapi.templating import Jinja2Templates
from elasticsearch import Elasticsearch
from pathlib import Path

# 앱 생성
app = FastAPI()

es_host = "localhost"
es_port = 9200

es = Elasticsearch(
    [{"host": es_host, "port": es_port, "scheme": "http"}],
    basic_auth=("elastic", "changeme"),
    request_timeout=300,  # 5min
    verify_certs=False
    # verify_certs: SSL 인증서를 검증할지 여부를 지정합니다. 여기서는 False로 설정되어 있어, 인증서 검증이 비활성화되어 있습니다.
    # 이러한 설정은 개발 또는 테스트 환경에서만 사용되어야 하며, 실제 운영 환경에서는 보안 위험으로 인해 사용되어서는 안 됩니다.
)

# 템플릿 엔진 설정
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

# 간단한 예제 데이터베이스 (실제로는 Elasticsearch, 데이터베이스 또는 다른 백엔드와 통합해야 함)
database = {
    1: "Python is a high-level programming language.",
    2: "FastAPI is a modern web framework for building APIs.",
    3: "Elasticsearch is a distributed search and analytics engine.",
}


# @app.post("/search/")
# async def search_post(request: Request):
#     # Elasticsearch에서 검색 실행
#     # body = {"query": {"match": {"text": query}}}
#     return templates.TemplateResponse("search_form.html", {"request": request})


@app.post("/search/")
@app.get("/search/")
async def search(
    request: Request,
    # query: Optional[str] = Form(None),
    query: str = Query(
        None, encoding="euc-kr", min_length=1
    ),  # 기본값을 None으로 설정하여 옵셔널로 만듦
):
    # async def read_item(item_id: str, q: Optional[str] = None):
    if query is None:
        # query 값이 None이면 유효성 검사를 통과하지 못한 것으로 처리
        return templates.TemplateResponse("search_form.html", {"request": request})

    # Elasticsearch에서 검색 실행
    # body = {"query": {"match": {"text": query}}}
    # body = {"query": {"match_all": {}}}
    body = {"query": {"match": {"station.name_full": query}}}

    # Elasticsearch로부터 검색 결과를 가져옴
    result = es.search(index="test2", body=body)

    # 결과를 가공하여 반환
    results = []
    for hit in result["hits"]["hits"]:
        results.append({"text": hit["_source"]})
        # results.append({"id": hit["_id"], "text": hit["_source"]["text"]})

    # 검색 결과를 HTML 템플릿으로 렌더링하여 반환
    return templates.TemplateResponse(
        "search_results.html", {"request": request, "results": results}
    )


# @app.get("/search/")
# async def search(query: str, request: Request):
#     # Elasticsearch에서 검색 실행
#     # body = {"query": {"match": {"text": query}}}
#     body = {"query": {"match_all": {}}}

#     # Elasticsearch로부터 검색 결과를 가져옴
#     result = es.search(index="test2", body=body)

#     # 결과를 가공하여 반환
#     results = []
#     for hit in result["hits"]["hits"]:
#         results.append({"id": hit["_id"], "text": hit["_source"]["text"]})

#     # 검색 결과를 HTML 템플릿으로 렌더링하여 반환
#     return templates.TemplateResponse(
#         "search_results.html", {"request": request, "results": results}
#     )


# @app.get("/search/")
# async def search(query: str):
#     # 검색어와 일치하는 결과를 반환
#     results = []
#     for key, value in database.items():
#         if query.lower() in value.lower():
#             results.append({"id": key, "text": value})
#     return {"results": results}


# @app.post("/")
# @app.get("/")
# async def search(
#     request: Request,
#     query: str = Form(...),  # 검색어를 Form 파라미터로 받습니다.
# ):
#     # Elasticsearch 쿼리 작성 (여기서는 단순한 풀 텍스트 검색 예제)
#     es_query = {"query": {"match": {"content": query}}}  # 검색 대상 필드와 검색어를 지정합니다.

#     # Elasticsearch에 쿼리 보내기
#     # search_results = es.search(index="your_index_name", body=es_query)

#     # # 검색 결과 추출
#     # hits = search_results["hits"]["hits"]
#     # search_results_list = [hit["_source"] for hit in hits]
#     search_results_list = ["test"]

#     return templates.TemplateResponse(
#         "search_results.html", {"request": request, "results": search_results_list}
#     )


# # FastAPI 앱을 실행합니다.
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)

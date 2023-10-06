# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
FROM python:3.10
WORKDIR /code

# APP_MODOLE 환경변수 설정
# ENV APP_MODULE app.app:app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# app 폴더 복사
COPY ./app /code/app
ENV PYTHONPATH=/app
# COPY ./start.sh /start.sh
# RUN /bin/sh -c chmod +x /start.sh

# 서버 생성
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# docker build -t myimage ./
FROM python:3.10.0-alpine
LABEL authors="kaixin"

RUN pip install --upgrade pip cos-python-sdk-v5 fastapi python-multipart uvicorn -i https://mirrors.aliyun.com/pypi/simple/

WORKDIR /app

COPY . /app

CMD ["uvicorn", "main:app", "--reload", "--host","0.0.0.0"]
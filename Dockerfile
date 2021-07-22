FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY . /app
WORKDIR /app

ENV settings=dev
# ENV WORKERS_PER_CORE=2



RUN apt-get update -y &&  pip install --upgrade pip &&  \
    apt-get install pipenv -y && pipenv install

CMD alembic upgrade heads
CMD python -m app.main


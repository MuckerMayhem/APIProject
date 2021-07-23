FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY . /app
WORKDIR /app

RUN apt-get update -y &&  pip install --upgrade pip \
    pip install -r requirements.txt

CMD alembic upgrade heads
CMD python -m app.main


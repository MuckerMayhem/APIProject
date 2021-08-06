upFROM python:3.9.1 as runtime
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONPATH /
EXPOSE 5001
RUN ls
#CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]
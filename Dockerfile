FROM python:3.8
COPY src/ app/src
COPY data/ app/data
WORKDIR /app/src
ENV DB_PASSWORD="password"
ENV DB_NAME="freetomove"
ENV DB_USER='master'


RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt 

CMD ["python", "main.py"]

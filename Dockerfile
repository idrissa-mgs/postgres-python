FROM python:3.8
ENV DB_PASSWORD="password"
ENV DB_NAME="freetomove"
ENV DB_USER='master'
ENV PATH="${PATH}:/root/.local/bin"

COPY src/requirements.txt requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt 


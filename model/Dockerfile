FROM python:latest

WORKDIR /usr/src/model

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

CMD [ "python", "./model.py" ]
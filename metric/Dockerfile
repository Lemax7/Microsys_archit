FROM python:latest

WORKDIR /usr/src/metric

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

CMD [ "python", "./metric.py" ]
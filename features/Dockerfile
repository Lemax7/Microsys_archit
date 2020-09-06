FROM python:latest

WORKDIR /usr/src/features

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ .

CMD [ "python", "./features.py" ]
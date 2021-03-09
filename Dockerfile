FROM python:3.9-buster

WORKDIR /usr/src/app

COPY . ./

RUN pip install -r ./requirements.txt

CMD ["python", "./app.py"]
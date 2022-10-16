FROM python:3.8-alpine

RUN pip install pipenv

WORKDIR /flasky
COPY . /flasky/

RUN pipenv install --system --deploy

CMD [ "python", "run.py"]

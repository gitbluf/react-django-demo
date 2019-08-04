FROM python:3.7.3-alpine3.10

LABEL maintainer="mrpetrovic@outlook.com" version="1.0"

RUN apk --no-cache add musl-dev linux-headers g++ \
    && pip install --upgrade pip \
    && pip install pipenv \
    && mkdir /code

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

CMD ["python", "./commerce/manage.py", "runserver", "0.0.0.0:8000"]

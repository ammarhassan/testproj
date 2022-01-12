FROM python:3.9-alpine

WORKDIR /code

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN apk update && apk add libpq-dev gcc musl-dev mariadb-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
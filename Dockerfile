FROM python:3.10.2-alpine
WORKDIR /src
COPY requirements.txt .
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt
COPY . .
CMD ["flask", "--app", "./src/contractual/api", "run", "--host", "0.0.0.0", "--port", "3003"]

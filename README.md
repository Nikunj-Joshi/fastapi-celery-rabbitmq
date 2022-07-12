# fastapi-celery-rabbitmq
Async Architecture with FastAPI, Celery, and RabbitMQ, Parallelism

### goto project source
```
cd ./fastapi-celery-rabbitmq
```

### run docker
```
docker-copose up -d
```

## Activate virtual environment where you created

### goto src dir
```
cd ./src
```

### run fastapi

```
uvicorn src.main:app --reload
```


### run celery **new terminal **activate virtual environment **in src dir 

```
celery -A main.celery worker --loglevel=info -Q universities,university
```

### run flower **new terminal **activate virtual environment **in src dir 

```
celery -A main.celery flower --port=5555
```
from fastapi import FastAPI

from src.config.celery_utils import create_celery
from src.routers import universities


def create_app() -> FastAPI:
    current_app = FastAPI(title="Asynchronous tasks processing with Celery and RabbitMQ",
                          description="Sample FastAPI Application to demonstrate Event "
                                      "driven architecture with Celery and RabbitMQ",
                          version="1.0.0", )

    current_app.celery_app = create_celery()
    current_app.include_router(universities.router)
    return current_app


app = create_app()
celery = app.celery_app


# if __name__ == "__main__":
# import uvicorn as uvicorn
#     uvicorn.run("main:app", port=9000, reload=True)
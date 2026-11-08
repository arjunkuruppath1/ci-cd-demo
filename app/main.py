
from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Demo API",
    description="Sample FastAPI application for learning CI/CD",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CI/CD Demo API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Arjun"
    }


from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "main page"}

@app.get("/user/{username}/{age}")
async def read_user(
    username: Annotated[str, Path(description="Enter username", min_length=5, max_length=20)],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    return {"message": f"User ID. NAME: {username}, AGE: {age}"}

@app.get("/user/{user_id}")
async def read_user_by_id(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]
):
    return {"message": f"USer data with ID: {user_id}"}



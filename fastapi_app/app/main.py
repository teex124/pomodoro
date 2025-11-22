from fastapi import FastAPI

app = FastAPI(title="My Dockerized FastAPI")

@app.get("/")
def read_root():
    return {"message": "Hello, Dockerized World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
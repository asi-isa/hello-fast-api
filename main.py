from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, world!"}


@app.get("/items/{item_id}")
async def get_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

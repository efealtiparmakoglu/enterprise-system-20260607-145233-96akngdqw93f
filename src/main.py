from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="API Gateway", version="1.0.0")

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None

items_db = []

@app.get("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/api/v1/items", response_model=List[Item])
def list_items(skip: int = 0, limit: int = 100):
    return items_db[skip:skip+limit]

@app.post("/api/v1/items", response_model=Item, status_code=201)
def create_item(item: Item):
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

@app.get("/api/v1/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/api/v1/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, existing in enumerate(items_db):
        if existing.id == item_id:
            item.id = item_id
            items_db[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/api/v1/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    global items_db
    items_db = [x for x in items_db if x.id != item_id]
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

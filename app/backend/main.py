from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uuid


app = FastAPI(title="Containerized App API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    quantity: int = 0


ITEMS_DB: List[Item] = []


@app.get("/")
async def root():
    return {
        "name": "Containerized App API",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}


@app.get("/items", response_model=List[Item])
async def list_items():
    return ITEMS_DB


@app.post("/items", response_model=Item)
async def create_item(item: Item):
    new_item = Item(
        id=str(uuid.uuid4()),
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity
    )
    ITEMS_DB.append(new_item)
    return new_item


@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: str):
    item = next((i for i in ITEMS_DB if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    index = next((i for i, x in enumerate(ITEMS_DB) if x.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_item = Item(
        id=item_id,
        name=item.name,
        description=item.description,
        price=item.price,
        quantity=item.quantity
    )
    ITEMS_DB[index] = updated_item
    return updated_item


@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    index = next((i for i, x in enumerate(ITEMS_DB) if x.id == item_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Item not found")
    ITEMS_DB.pop(index)
    return {"message": "Item deleted"}

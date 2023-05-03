from fastapi import FastAPI
from pydantic import BaseModel, Field
import redis

pool = redis.ConnectionPool(host='red-ch90qs5gk4qeoo1326pg', port=6379, db=0)
redis = redis.Redis(connection_pool=pool)
redis.set("Used", 0)


class Order(BaseModel):
    id: int
    item: str
    quantity: int = Field(gt=0, description="The quantity must be greater than zero")
    price: float = Field(gt=0, description="The price must be greater than zero")
    status: str

    def __int__(self, item, quantity, price, status):
        self.item = item
        self.quantity = quantity
        self.price = price
        self.status = status

    def __str__(self):
        return self.item

    def __repr__(self):
        return f"Order({self.item})"

    def revenue(self):
        return self.quantity * self.price


class BodyInput(BaseModel):
    orders: list[Order]
    criterion: str

    def all_revenue(self, criterion: str):
        output = 0.00
        for o in self.orders:
            if o.status == criterion or criterion == "all":
                output += o.revenue()
        return round(output, 2)


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/solution")
async def process_orders(payload: BodyInput) -> str:
    key = str(payload.json())
    if redis.exists(key):
        last = int(redis.get("Used"))
        redis.set("Used", str(last + 1))
        return redis.get(key)
    redis.set(key, str(payload.all_revenue(payload.criterion)))
    output = payload.all_revenue(payload.criterion)
    return str(output)

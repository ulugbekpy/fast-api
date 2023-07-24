from typing import Union

from fastapi import FastAPI

from models import Item,Student

app = FastAPI()

students_data = [
    {
        'name':"ulugbek",
        'age':21,
        'university':'TSUE',
        'is_uzbek':True
    }
]



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("items/create/")
def create_item(item_id: int, item_name: str, item_price: float):
    return {"item_name": item_name, "item_price": item_price}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/students/register/")
def register_student(student:Student):
    students_data.append(student)
    return f'{student.name} added'
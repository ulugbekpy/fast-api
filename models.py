from pydantic import BaseModel
from typing import Union


class Student(BaseModel):
    name:str
    course:int
    university:str
    is_uzbek:bool


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
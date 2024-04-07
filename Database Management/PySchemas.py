from pydantic import BaseModel

class MenuItem(BaseModel):

    id_:int
    name:str
    description:str
    price:int
    class Config:
        orm_mode = True

class Pasta(MenuItem):

    pasta_type:str
    portion:int
    addition:str
    time:int


class Drink(MenuItem):

    drink_type:str
    size:float





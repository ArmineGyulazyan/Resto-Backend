from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from Database import DB_Session, Engine
from typing import Dict, List
# from alembic.config import Config
# from alembic import command
import CRUD, DBModels, PySchemas
import uvicorn

DBModels.Base.metadata.create_all(bind=Engine)
app = FastAPI()

# alembic_mig = Config('alembic.ini')
#
# @app.on_event('startup')
# async def startup_event():
#     command.upgrade(alembic_mig, 'head')


def get_db():
    db = DB_Session()
    try:
        yield db
    finally:
        db.close()


@app.post('/create_pasta', response_model=None, status_code=201)
async def create_pasta(item:PySchemas.Pasta, db:Session=Depends(get_db)):
    CRUD.create_item(db,item)


@app.post('/create_drink', response_model=None, status_code=201)
async def create_drink(item:PySchemas.Drink, db:Session=Depends(get_db)):
    CRUD.create_item(db,item)


@app.get('/pastas', response_model=List[PySchemas.Pasta], status_code=201)
async def read_pastas(db:Session=Depends(get_db)):
    db_items = CRUD.get_pastas(db)
    return db_items


@app.get('/drinks', response_model=List[PySchemas.Drink], status_code=201)
async def read_drinks(db:Session=Depends(get_db)):
    db_items = CRUD.get_drinks(db)
    return db_items


@app.put('/update_pasta/{pasta_id}', response_model=None, status_code=200)
async def update_pasta(pasta_id:int, item:PySchemas.Pasta, db:Session=Depends(get_db),new_args:Dict=None):
    CRUD.update_item(db,pasta_id,item,new_args)


@app.put('/update_drink/{drink_id}', response_model=None, status_code=200)
async def update_drink(drink_id:int, item:PySchemas.Drink, db:Session=Depends(get_db),new_args:Dict=None):
    CRUD.update_item(db,drink_id,item,new_args)


@app.delete('/delete_pasta/{pasta_id}', response_model=None, status_code=204)
async def delete_pasta(pasta_id:int, item:PySchemas.Pasta, db:Session=Depends(get_db)):
    CRUD.delete_item(db,pasta_id,item)


@app.delete('/delete_drink/{drink_id}', response_model=None, status_code=204)
async def delete_drink(drink_id:int, item:PySchemas.Drink, db:Session=Depends(get_db)):
    CRUD.delete_item(db,drink_id,item)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
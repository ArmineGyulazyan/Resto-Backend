from sqlalchemy.orm import Session
from typing import Dict
import DBModels, PySchemas


def create_item(db:Session, item_obj:PySchemas.MenuItem):
    if isinstance(item_obj, PySchemas.Pasta):
        db_item = DBModels.Pasta(name=item_obj.name, description=item_obj.description, pasta_type=item_obj.pasta_type,
                               portion=item_obj.portion, addition=item_obj.addition, time=item_obj.time, price=item_obj.price)
    else:
        db_item = DBModels.Drink(name=item_obj.name, description=item_obj.description, drink_type=item_obj.drink_type,
                                 size=item_obj.size, price=item_obj.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)


def get_pastas(db:Session):
    return db.query(DBModels.Pasta).all()


def get_drinks(db:Session):
    return db.query(DBModels.Drink).all()


def update_item(db:Session, item_id:int, item_obj:PySchemas.MenuItem, new_args:Dict):
    cls_name = DBModels.Pasta if isinstance(item_obj, PySchemas.Pasta) else DBModels.Drink
    db_item = db.query(cls_name).filter(cls_name.id_==item_id).first()
    if db_item:
        for key, val in new_args.items():
            setattr(db_item, key, val)
        db.commit()
        db.refresh(db_item)


def delete_item(db:Session, item_id:int, item_obj:PySchemas.MenuItem):
    cls_name = DBModels.Pasta if isinstance(item_obj, PySchemas.Pasta) else DBModels.Drink
    db_item = db.query(cls_name).filter(cls_name.id_ == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()












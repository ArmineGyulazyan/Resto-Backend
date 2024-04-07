from sqlalchemy import Column, Integer, Float, String
from Database import Base, Engine

class Pasta(Base):

    __tablename__ = 'pastas'

    id_ = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    pasta_type = Column(String, index=True)
    portion = Column(Integer, index=True)
    addition = Column(String, index=True)
    time = Column(Integer, index=True)
    price = Column(Integer, index=True)


class Drink(Base):

    __tablename__ = 'drinks'

    id_ = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    drink_type = Column(String, index=True)
    size = Column(Float, index=True)
    price = Column(Integer, index=True)


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///./menu_items.db', connect_args = {'check_same_thread': False})
DB_Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()


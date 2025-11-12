# import os
# from dotenv import load_dotenv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker 
# from sqlalchemy.ext.declarative import declarative_base
# ---------------------------------
import os
from dotenv import load_dotenv
load_dotenv()
MySQL_URL = os.getenv('DB_URL')
# ----------------------------------
from sqlalchemy import create_engine
Mysql_Engine = create_engine(MySQL_URL)
# ----------------------------------
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(autocommit=False, autoflush=False, bind=Mysql_Engine)
# ----------------------------------
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# ----------------------------------
# function get_db()
async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

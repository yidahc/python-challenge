## Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
# Connecting to postgress

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
# engine gives SQA the power to create/edit tables

Session = sessionmaker(bind=engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
## Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
# Connecting to postgress

import os
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'



#engine = create_engine(DATABASE_URI)
# engine gives SQA the power to create/edit tables on postgress

#Session = sessionmaker(bind=engine)

#def recreate_database():
#    Base.metadata.drop_all(engine)
#    Base.metadata.create_all(engine)
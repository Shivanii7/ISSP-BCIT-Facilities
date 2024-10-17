import sys
from models import *
import sqlalchemy
import mysql.connector
import yaml
# Set up an engine
# Factory function to get a session bound to the DB engine
with open('user.yml', 'r') as f:
    user = yaml.safe_load(f.read())
    
DB_ENGINE = sqlalchemy.create_engine(f"mysql+mysqldb://{user['datastore']['user']}:{user['datastore']['password']}@{user['datastore']['hostname']}:{user['datastore']['port']}/{user['datastore']['db']}")
# USE THIS IF YOU HAVE DOCKER AND WANNA USE THE SQLDOCKER.PY


# DB_ENGINE = sqlalchemy.create_engine("sqlite:///database.db") 
# USE THIS IF YOU DON'T WANNA USE A DONCKER CONTAINER
from sqlalchemy.orm import sessionmaker
def make_session():
    return sessionmaker(bind=DB_ENGINE)
if __name__=="__main__":
    make_session()

def create_tables():
    Base.metadata.create_all(DB_ENGINE)
def drop_tables():
    Base.metadata.drop_all(DB_ENGINE)
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "drop":
        drop_tables()
    else:
        create_tables()
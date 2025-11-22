from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings


settings = Settings() 


def get_session():
    database_url = settings.DB_PATH
    engine = create_engine(database_url)
    session = sessionmaker(engine)
    return session
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DRIVER: str = 'postgresql+psycopg2'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 4578
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_NAME: str = 'pomidoro_db'
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    @property
    def database_url(self) -> str:
        return f'{self.DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
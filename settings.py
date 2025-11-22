from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = 'asdasgadsadfgsd123'
    DB_PATH: str = 'postgresql+psycopg2://zirael:12356@localhost:4578/pomodoro'
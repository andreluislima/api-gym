from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL:str = Field(default='postgresql+asyncpg://workout:workout@172.26.33.239:5432/workout')
    
settings = Settings()

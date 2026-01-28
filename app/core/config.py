from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL_ASYNC: str = "sqlite+aiosqlite:///./dev.db"
    DATABASE_URL_SYNC:str="sqlite:///./ecom.db"

    
    class Config:
        env_file = ".env"
        
        
settings = Settings()
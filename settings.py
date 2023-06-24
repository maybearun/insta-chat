from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    model: str = 'gpt-3.5-turbo'
    user: str = 'user'
    username :str
    password :str
    class Config:
        env_file = ".env"
settings = Settings()
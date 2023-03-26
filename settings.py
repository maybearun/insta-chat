from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    url: str
    model: str = 'gpt-3.5-turbo'
    user: str = 'user'

    class Config:
        env_file = ".env"
settings = Settings()
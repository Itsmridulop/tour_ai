from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str
    COLLECTION_NAME: str

    model_config = SettingsConfigDict(env_file=".config.env")

settings = Settings()

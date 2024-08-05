from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PREFIX_URL: str
    PIXABAY_API_KEY: str

    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8')


settings = Settings()

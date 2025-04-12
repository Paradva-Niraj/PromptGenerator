from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    GEMINI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

config = Config()
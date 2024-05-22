import logging

from pydantic import SecretStr
from pydantic_settings import BaseSettings
from urllib.parse import quote


class Settings(BaseSettings):
    # Environment
    env: str
   
    # API INFO
    api_name: str
    api_version: str
    api_root_path: str

    # Nawi API's
    nawi_reports_api_url: str

    # Dock API's
    dock_authorization_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'
        case_sensitive = False


settings = Settings()
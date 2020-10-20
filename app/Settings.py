from typing import List, Optional

import yaml
from pydantic import BaseSettings, Field
from yaml import Loader


class Settings(BaseSettings):
    name: str = Field(...)
    debug: Optional[int] = Field(None)
    sources: List[str] = Field(...)
    redis_port: int = Field(...)
    clearcache: str = Field(...)


settings_instance = None


def settings_from_yaml(filename):
    global settings_instance
    if settings_instance is None:
        with open(filename) as file:
            settings_instance = Settings(**yaml.load(file, Loader=Loader))
    return settings_instance

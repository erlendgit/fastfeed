from typing import Iterable, Optional, List

import yaml
from pydantic import BaseSettings, Field
from yaml import Loader


class Settings(BaseSettings):
    name: str = Field(...)
    sources: List[str] = Field(...)
    redis_port: int = Field(...)


settings_instance = None


def settings_from_yaml(filename):
    global settings_instance
    if settings_instance is None:
        with open(filename) as file:
            settings_instance = Settings(**yaml.load(file, Loader=Loader))
    return settings_instance

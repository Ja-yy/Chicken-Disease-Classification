from typing import TypeVar

from pydantic_settings import BaseSettings

ConfigType = TypeVar("ConfigType", bound=BaseSettings)

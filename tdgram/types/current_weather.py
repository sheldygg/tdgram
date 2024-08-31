from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CurrentWeather(BaseType):
    """
    Describes the current weather
    """

    __type__: Literal["currentWeather"] = "currentWeather"

    temperature: float
    """Temperature, in degree Celsius"""
    emoji: str
    """Emoji representing the weather"""

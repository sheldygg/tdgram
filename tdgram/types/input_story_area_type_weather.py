from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputStoryAreaTypeWeather(BaseType):
    """
    An area with information about weather
    """

    __type__: Literal["inputStoryAreaTypeWeather"] = "inputStoryAreaTypeWeather"

    temperature: float
    """Temperature, in degree Celsius"""
    emoji: str
    """Emoji representing the weather"""
    background_color: int
    """A color of the area background in the ARGB format"""

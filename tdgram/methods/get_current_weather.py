from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CurrentWeather, Location
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCurrentWeather(BaseMethod):
    """
    Returns the current weather in the given location
    """

    __type__: Literal["getCurrentWeather"] = "getCurrentWeather"
    __returning_type__ = CurrentWeather

    location: Location
    """The location"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Location(BaseType):
    """
    Describes a location on planet Earth
    """

    __type__: Literal["location"] = "location"

    latitude: float
    """Latitude of the location in degrees; as defined by the sender"""
    longitude: float
    """Longitude of the location, in degrees; as defined by the sender"""
    horizontal_accuracy: float
    """The estimated horizontal accuracy of the location, in meters; as defined by the sender. 0 if unknown"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class InputMessageLocation(BaseType):
    """
    A message with a location
    """

    __type__: Literal["inputMessageLocation"] = "inputMessageLocation"

    location: Location
    """Location to be sent"""
    live_period: int
    """Period for which the location can be updated, in seconds; must be between 60 and 86400 for a temporary live location, 0x7FFFFFFF for permanent live location, and 0 otherwise"""
    heading: int
    """For live locations, a direction in which the location moves, in degrees; 1-360. Pass 0 if unknown"""
    proximity_alert_radius: int
    """For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled. Can't be enabled in channels and Saved Messages"""

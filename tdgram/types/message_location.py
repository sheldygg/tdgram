from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Location


@dataclass(kw_only=True)
class MessageLocation(BaseType):
    """
    A message with a location
    """

    __type__: Literal["messageLocation"] = "messageLocation"

    location: Location
    """The location description"""
    live_period: int
    """Time relative to the message send date, for which the location can be updated, in seconds; if 0x7FFFFFFF, then location can be updated forever"""
    expires_in: int
    """Left time for which the location can be updated, in seconds. If 0, then the location can't be updated anymore. The update updateMessageContent is not sent when this field changes"""
    heading: int
    """For live locations, a direction in which the location moves, in degrees; 1-360. If 0 the direction is unknown"""
    proximity_alert_radius: int
    """For live locations, a maximum distance to another chat member for proximity alerts, in meters (0-100000). 0 if the notification is disabled. Available only to the message sender"""

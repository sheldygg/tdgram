from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Location, Message, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageLiveLocation(BaseMethod):
    """
    Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location.
    """

    __type__: Literal["editMessageLiveLocation"] = "editMessageLiveLocation"
    __returning_type__ = Message

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_be_edited to check whether the message can be edited"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none; for bots only"""
    location: Location | None = None
    """New location content of the message; pass null to stop sharing the live location"""
    live_period: int
    """New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever."""
    heading: int
    """The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown"""
    proximity_alert_radius: int
    """The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled"""

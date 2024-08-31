from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Location, Ok, ReplyMarkup
from .base import BaseMethod


@dataclass(kw_only=True)
class EditInlineMessageLiveLocation(BaseMethod):
    """
    Edits the content of a live location in an inline message sent via a bot; for bots only
    """

    __type__: Literal["editInlineMessageLiveLocation"] = "editInlineMessageLiveLocation"
    __returning_type__ = Ok

    inline_message_id: str
    """Inline message identifier"""
    reply_markup: ReplyMarkup | None = None
    """The new message reply markup; pass null if none"""
    location: Location | None = None
    """New location content of the message; pass null to stop sharing the live location"""
    live_period: int
    """New time relative to the message send date, for which the location can be updated, in seconds. If 0x7FFFFFFF specified, then the location can be updated forever."""
    heading: int
    """The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown"""
    proximity_alert_radius: int
    """The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import JsonValue, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SaveApplicationLogEvent(BaseMethod):
    """
    Saves application log event on the server. Can be called before authorization
    """

    __type__: Literal["saveApplicationLogEvent"] = "saveApplicationLogEvent"
    __returning_type__ = Ok

    type: str
    """Event type"""
    chat_id: int
    """Optional chat identifier, associated with the event"""
    data: JsonValue
    """The log event data"""

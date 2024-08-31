from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatLocation, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatLocation(BaseMethod):
    """
    Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
    """

    __type__: Literal["setChatLocation"] = "setChatLocation"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    location: ChatLocation
    """New location for the chat; must be valid and not null"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessMessageIsPinned(BaseMethod):
    """
    Pins or unpins a message sent on behalf of a business account; for bots only
    """

    __type__: Literal["setBusinessMessageIsPinned"] = "setBusinessMessageIsPinned"
    __returning_type__ = Ok

    business_connection_id: str
    """Unique identifier of business connection on behalf of which the message was sent"""
    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message"""
    is_pinned: bool
    """Pass true to pin the message, pass false to unpin it"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageReadDate
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageReadDate(BaseMethod):
    """
    Returns read date of a recent outgoing message in a private chat. The method can be called if messageProperties.can_get_read_date == true
    """

    __type__: Literal["getMessageReadDate"] = "getMessageReadDate"
    __returning_type__ = MessageReadDate

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Identifier of the message"""

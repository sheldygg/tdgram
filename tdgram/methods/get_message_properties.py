from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageProperties
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageProperties(BaseMethod):
    """
    Returns properties of a message; this is an offline request
    """

    __type__: Literal["getMessageProperties"] = "getMessageProperties"
    __returning_type__ = MessageProperties

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Identifier of the message"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatChangeTitle(BaseType):
    """
    An updated chat title
    """

    __type__: Literal["messageChatChangeTitle"] = "messageChatChangeTitle"

    title: str
    """New chat title"""

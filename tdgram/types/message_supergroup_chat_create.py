from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSupergroupChatCreate(BaseType):
    """
    A newly created supergroup or channel
    """

    __type__: Literal["messageSupergroupChatCreate"] = "messageSupergroupChatCreate"

    title: str
    """Title of the supergroup or channel"""

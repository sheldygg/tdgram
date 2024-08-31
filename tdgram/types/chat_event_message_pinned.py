from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class ChatEventMessagePinned(BaseType):
    """
    A message was pinned
    """

    __type__: Literal["chatEventMessagePinned"] = "chatEventMessagePinned"

    message: Message
    """Pinned message"""

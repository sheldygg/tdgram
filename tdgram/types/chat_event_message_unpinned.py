from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class ChatEventMessageUnpinned(BaseType):
    """
    A message was unpinned
    """

    __type__: Literal["chatEventMessageUnpinned"] = "chatEventMessageUnpinned"

    message: Message
    """Unpinned message"""

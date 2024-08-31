from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatEvent


@dataclass(kw_only=True)
class ChatEvents(BaseType):
    """
    Contains a list of chat events
    """

    __type__: Literal["chatEvents"] = "chatEvents"

    events: list[ChatEvent]
    """List of events"""

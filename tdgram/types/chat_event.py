from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatEventAction, MessageSender


@dataclass(kw_only=True)
class ChatEvent(BaseType):
    """
    Represents a chat event
    """

    __type__: Literal["chatEvent"] = "chatEvent"

    id: int
    """Chat event identifier"""
    date: int
    """Point in time (Unix timestamp) when the event happened"""
    member_id: MessageSender
    """Identifier of the user or chat who performed the action"""
    action: ChatEventAction
    """The action"""

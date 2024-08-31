from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList, ChatSource


@dataclass(kw_only=True)
class ChatPosition(BaseType):
    """
    Describes a position of a chat in a chat list
    """

    __type__: Literal["chatPosition"] = "chatPosition"

    list: ChatList
    """The chat list"""
    order: int
    """A parameter used to determine order of the chat in the chat list. Chats must be sorted by the pair (order, chat.id) in descending order"""
    is_pinned: bool
    """True, if the chat is pinned in the chat list"""
    source: ChatSource | None = None
    """Source of the chat in the chat list; may be null"""

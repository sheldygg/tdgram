from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList


@dataclass(kw_only=True)
class UpdateChatRemovedFromList(BaseType):
    """
    A chat was removed from a chat list
    """

    __type__: Literal["updateChatRemovedFromList"] = "updateChatRemovedFromList"

    chat_id: int
    """Chat identifier"""
    chat_list: ChatList
    """The chat list from which the chat was removed"""

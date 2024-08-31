from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList


@dataclass(kw_only=True)
class UpdateChatAddedToList(BaseType):
    """
    A chat was added to a chat list
    """

    __type__: Literal["updateChatAddedToList"] = "updateChatAddedToList"

    chat_id: int
    """Chat identifier"""
    chat_list: ChatList
    """The chat list to which the chat was added"""

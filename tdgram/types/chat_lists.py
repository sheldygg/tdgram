from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList


@dataclass(kw_only=True)
class ChatLists(BaseType):
    """
    Contains a list of chat lists
    """

    __type__: Literal["chatLists"] = "chatLists"

    chat_lists: list[ChatList]
    """List of chat lists"""

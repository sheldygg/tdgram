from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatListFolder(BaseType):
    """
    A list of chats added to a chat folder
    """

    __type__: Literal["chatListFolder"] = "chatListFolder"

    chat_folder_id: int
    """Chat folder identifier"""

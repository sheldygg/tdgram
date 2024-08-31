from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolder, Count
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolderChatCount(BaseMethod):
    """
    Returns approximate number of chats in a being created chat folder. Main and archive chat lists must be fully preloaded for this function to work correctly
    """

    __type__: Literal["getChatFolderChatCount"] = "getChatFolderChatCount"
    __returning_type__ = Count

    folder: ChatFolder
    """The new chat folder"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatFolderInfo


@dataclass(kw_only=True)
class UpdateChatFolders(BaseType):
    """
    The list of chat folders or a chat folder has changed
    """

    __type__: Literal["updateChatFolders"] = "updateChatFolders"

    chat_folders: list[ChatFolderInfo]
    """The new list of chat folders"""
    main_chat_list_position: int
    """Position of the main chat list among chat folders, 0-based"""
    are_tags_enabled: bool
    """True, if folder tags are enabled"""

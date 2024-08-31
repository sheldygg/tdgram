from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReorderChatFolders(BaseMethod):
    """
    Changes the order of chat folders
    """

    __type__: Literal["reorderChatFolders"] = "reorderChatFolders"
    __returning_type__ = Ok

    chat_folder_ids: list[int]
    """Identifiers of chat folders in the new correct order"""
    main_chat_list_position: int
    """Position of the main chat list among chat folders, 0-based. Can be non-zero only for Premium users"""

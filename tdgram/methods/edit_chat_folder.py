from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolder, ChatFolderInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class EditChatFolder(BaseMethod):
    """
    Edits existing chat folder. Returns information about the edited chat folder
    """

    __type__: Literal["editChatFolder"] = "editChatFolder"
    __returning_type__ = ChatFolderInfo

    chat_folder_id: int
    """Chat folder identifier"""
    folder: ChatFolder
    """The edited chat folder"""

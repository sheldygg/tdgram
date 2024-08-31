from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolder, ChatFolderInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateChatFolder(BaseMethod):
    """
    Creates new chat folder. Returns information about the created chat folder. There can be up to getOption('chat_folder_count_max') chat folders, but the limit can be increased with Telegram Premium
    """

    __type__: Literal["createChatFolder"] = "createChatFolder"
    __returning_type__ = ChatFolderInfo

    folder: ChatFolder
    """The new chat folder"""

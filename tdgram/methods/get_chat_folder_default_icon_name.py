from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolder, ChatFolderIcon
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolderDefaultIconName(BaseMethod):
    """
    Returns default icon name for a folder. Can be called synchronously
    """

    __type__: Literal["getChatFolderDefaultIconName"] = "getChatFolderDefaultIconName"
    __returning_type__ = ChatFolderIcon

    folder: ChatFolder
    """Chat folder"""

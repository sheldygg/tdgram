from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolder
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolder(BaseMethod):
    """
    Returns information about a chat folder by its identifier
    """

    __type__: Literal["getChatFolder"] = "getChatFolder"
    __returning_type__ = ChatFolder

    chat_folder_id: int
    """Chat folder identifier"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatFolder(BaseMethod):
    """
    Deletes existing chat folder
    """

    __type__: Literal["deleteChatFolder"] = "deleteChatFolder"
    __returning_type__ = Ok

    chat_folder_id: int
    """Chat folder identifier"""
    leave_chat_ids: list[int]
    """Identifiers of the chats to leave. The chats must be pinned or always included in the folder"""

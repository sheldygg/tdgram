from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatHistory(BaseMethod):
    """
    Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat
    """

    __type__: Literal["deleteChatHistory"] = "deleteChatHistory"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    remove_from_chat_list: bool
    """Pass true to remove the chat from all chat lists"""
    revoke: bool
    """Pass true to delete chat history for all users"""

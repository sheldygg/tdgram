from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatIsPinned(BaseMethod):
    """
    Changes the pinned state of a chat. There can be up to getOption('pinned_chat_count_max')/getOption('pinned_archived_chat_count_max') pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium
    """

    __type__: Literal["toggleChatIsPinned"] = "toggleChatIsPinned"
    __returning_type__ = Ok

    chat_list: ChatList
    """Chat list in which to change the pinned state of the chat"""
    chat_id: int
    """Chat identifier"""
    is_pinned: bool
    """Pass true to pin the chat; pass false to unpin it"""

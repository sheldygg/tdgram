from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteMessages(BaseMethod):
    """
    Deletes messages
    """

    __type__: Literal["deleteMessages"] = "deleteMessages"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_ids: list[int]
    """Identifiers of the messages to be deleted. Use messageProperties.can_be_deleted_only_for_self and messageProperties.can_be_deleted_for_all_users to get suitable messages"""
    revoke: bool
    """Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats"""

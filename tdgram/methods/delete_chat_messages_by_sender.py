from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSender, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatMessagesBySender(BaseMethod):
    """
    Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges
    """

    __type__: Literal["deleteChatMessagesBySender"] = "deleteChatMessagesBySender"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    sender_id: MessageSender
    """Identifier of the sender of messages to delete"""

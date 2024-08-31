from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatMember, MessageSender
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatMember(BaseMethod):
    """
    Returns information about a single member of a chat
    """

    __type__: Literal["getChatMember"] = "getChatMember"
    __returning_type__ = ChatMember

    chat_id: int
    """Chat identifier"""
    member_id: MessageSender
    """Member identifier"""

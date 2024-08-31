from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TransferChatOwnership(BaseMethod):
    """
    Changes the owner of a chat; requires owner privileges in the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats
    """

    __type__: Literal["transferChatOwnership"] = "transferChatOwnership"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    user_id: int
    """Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user"""
    password: str
    """The 2-step verification password of the current user"""

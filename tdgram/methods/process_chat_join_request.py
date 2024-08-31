from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ProcessChatJoinRequest(BaseMethod):
    """
    Handles a pending join request in a chat
    """

    __type__: Literal["processChatJoinRequest"] = "processChatJoinRequest"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    user_id: int
    """Identifier of the user that sent the request"""
    approve: bool
    """Pass true to approve the request; pass false to decline it"""

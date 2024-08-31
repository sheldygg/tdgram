from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostStatus
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoostStatus(BaseMethod):
    """
    Returns the current boost status for a supergroup or a channel chat
    """

    __type__: Literal["getChatBoostStatus"] = "getChatBoostStatus"
    __returning_type__ = ChatBoostStatus

    chat_id: int
    """Identifier of the chat"""

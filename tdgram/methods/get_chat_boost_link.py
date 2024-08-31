from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatBoostLink
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatBoostLink(BaseMethod):
    """
    Returns an HTTPS link to boost the specified supergroup or channel chat
    """

    __type__: Literal["getChatBoostLink"] = "getChatBoostLink"
    __returning_type__ = ChatBoostLink

    chat_id: int
    """Identifier of the chat"""

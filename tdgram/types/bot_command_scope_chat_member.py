from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeChatMember(BaseType):
    """
    A scope covering a member of a chat
    """

    __type__: Literal["botCommandScopeChatMember"] = "botCommandScopeChatMember"

    chat_id: int
    """Chat identifier"""
    user_id: int
    """User identifier"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeChat(BaseType):
    """
    A scope covering all members of a chat
    """

    __type__: Literal["botCommandScopeChat"] = "botCommandScopeChat"

    chat_id: int
    """Chat identifier"""

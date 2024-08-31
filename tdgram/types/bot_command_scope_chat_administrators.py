from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeChatAdministrators(BaseType):
    """
    A scope covering all administrators of a chat
    """

    __type__: Literal["botCommandScopeChatAdministrators"] = "botCommandScopeChatAdministrators"

    chat_id: int
    """Chat identifier"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeAllPrivateChats(BaseType):
    """
    A scope covering all private chats
    """

    __type__: Literal["botCommandScopeAllPrivateChats"] = "botCommandScopeAllPrivateChats"

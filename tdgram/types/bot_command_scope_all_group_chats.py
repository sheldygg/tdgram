from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeAllGroupChats(BaseType):
    """
    A scope covering all group and supergroup chats
    """

    __type__: Literal["botCommandScopeAllGroupChats"] = "botCommandScopeAllGroupChats"

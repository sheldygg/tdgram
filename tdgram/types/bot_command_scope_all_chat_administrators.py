from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeAllChatAdministrators(BaseType):
    """
    A scope covering all group and supergroup chat administrators
    """

    __type__: Literal["botCommandScopeAllChatAdministrators"] = (
        "botCommandScopeAllChatAdministrators"
    )

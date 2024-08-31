from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BotCommandScopeDefault(BaseType):
    """
    A scope covering all users
    """

    __type__: Literal["botCommandScopeDefault"] = "botCommandScopeDefault"

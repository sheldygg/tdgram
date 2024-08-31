from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventActiveUsernamesChanged(BaseType):
    """
    The chat active usernames were changed
    """

    __type__: Literal["chatEventActiveUsernamesChanged"] = "chatEventActiveUsernamesChanged"

    old_usernames: list[str]
    """Previous list of active usernames"""
    new_usernames: list[str]
    """New list of active usernames"""

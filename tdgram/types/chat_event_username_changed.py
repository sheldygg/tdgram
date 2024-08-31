from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventUsernameChanged(BaseType):
    """
    The chat editable username was changed
    """

    __type__: Literal["chatEventUsernameChanged"] = "chatEventUsernameChanged"

    old_username: str
    """Previous chat username"""
    new_username: str
    """New chat username"""

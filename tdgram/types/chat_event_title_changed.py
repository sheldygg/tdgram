from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventTitleChanged(BaseType):
    """
    The chat title was changed
    """

    __type__: Literal["chatEventTitleChanged"] = "chatEventTitleChanged"

    old_title: str
    """Previous chat title"""
    new_title: str
    """New chat title"""

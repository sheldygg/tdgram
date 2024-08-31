from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionWatchingAnimations(BaseType):
    """
    The user is watching animations sent by the other party by clicking on an animated emoji
    """

    __type__: Literal["chatActionWatchingAnimations"] = "chatActionWatchingAnimations"

    emoji: str
    """The animated emoji"""

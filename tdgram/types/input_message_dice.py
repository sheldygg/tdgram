from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputMessageDice(BaseType):
    """
    A dice message
    """

    __type__: Literal["inputMessageDice"] = "inputMessageDice"

    emoji: str
    """Emoji on which the dice throw animation is based"""
    clear_draft: bool
    """True, if the chat message draft must be deleted"""

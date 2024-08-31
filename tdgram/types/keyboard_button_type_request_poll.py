from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeRequestPoll(BaseType):
    """
    A button that allows the user to create and send a poll when pressed; available only in private chats
    """

    __type__: Literal["keyboardButtonTypeRequestPoll"] = "keyboardButtonTypeRequestPoll"

    force_regular: bool
    """If true, only regular polls must be allowed to create"""
    force_quiz: bool
    """If true, only polls in quiz mode must be allowed to create"""

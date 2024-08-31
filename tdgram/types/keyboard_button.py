from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import KeyboardButtonType


@dataclass(kw_only=True)
class KeyboardButton(BaseType):
    """
    Represents a single button in a bot keyboard
    """

    __type__: Literal["keyboardButton"] = "keyboardButton"

    text: str
    """Text of the button"""
    type: KeyboardButtonType
    """Type of the button"""

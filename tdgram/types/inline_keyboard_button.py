from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InlineKeyboardButtonType


@dataclass(kw_only=True)
class InlineKeyboardButton(BaseType):
    """
    Represents a single button in an inline keyboard
    """

    __type__: Literal["inlineKeyboardButton"] = "inlineKeyboardButton"

    text: str
    """Text of the button"""
    type: InlineKeyboardButtonType
    """Type of the button"""

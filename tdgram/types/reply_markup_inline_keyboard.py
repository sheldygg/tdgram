from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InlineKeyboardButton


@dataclass(kw_only=True)
class ReplyMarkupInlineKeyboard(BaseType):
    """
    Contains an inline keyboard layout
    """

    __type__: Literal["replyMarkupInlineKeyboard"] = "replyMarkupInlineKeyboard"

    rows: list[list[InlineKeyboardButton]]
    """A list of rows of inline keyboard buttons"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import KeyboardButton


@dataclass(kw_only=True)
class ReplyMarkupShowKeyboard(BaseType):
    """
    Contains a custom keyboard layout to quickly reply to bots
    """

    __type__: Literal["replyMarkupShowKeyboard"] = "replyMarkupShowKeyboard"

    rows: list[list[KeyboardButton]]
    """A list of rows of bot keyboard buttons"""
    is_persistent: bool
    """True, if the keyboard is supposed to always be shown when the ordinary keyboard is hidden"""
    resize_keyboard: bool
    """True, if the application needs to resize the keyboard vertically"""
    one_time: bool
    """True, if the application needs to hide the keyboard after use"""
    is_personal: bool
    """True, if the keyboard must automatically be shown to the current user. For outgoing messages, specify true to show the keyboard only for the mentioned users and for the target user of a reply"""
    input_field_placeholder: str | None = None
    """If non-empty, the placeholder to be shown in the input field when the keyboard is active; 0-64 characters"""

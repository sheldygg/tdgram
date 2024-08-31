from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TargetChat


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeSwitchInline(BaseType):
    """
    A button that forces an inline query to the bot to be inserted in the input field
    """

    __type__: Literal["inlineKeyboardButtonTypeSwitchInline"] = (
        "inlineKeyboardButtonTypeSwitchInline"
    )

    query: str
    """Inline query to be sent to the bot"""
    target_chat: TargetChat
    """Target chat from which to send the inline query"""

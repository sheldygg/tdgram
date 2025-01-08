from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeCopyText(BaseType):
    """
    A button that copies specified text to clipboard
    """

    __type__: Literal["inlineKeyboardButtonTypeCopyText"] = "inlineKeyboardButtonTypeCopyText"

    text: str
    """The text to copy to clipboard"""

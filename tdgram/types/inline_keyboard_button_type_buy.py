from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InlineKeyboardButtonTypeBuy(BaseType):
    """
    A button to buy something. This button must be in the first column and row of the keyboard and can be attached only to a message with content of the type messageInvoice
    """

    __type__: Literal["inlineKeyboardButtonTypeBuy"] = "inlineKeyboardButtonTypeBuy"

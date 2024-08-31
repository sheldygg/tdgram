from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeText(BaseType):
    """
    A simple button, with text that must be sent when the button is pressed
    """

    __type__: Literal["keyboardButtonTypeText"] = "keyboardButtonTypeText"

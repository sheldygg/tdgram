from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeRequestLocation(BaseType):
    """
    A button that sends the user's location when pressed; available only in private chats
    """

    __type__: Literal["keyboardButtonTypeRequestLocation"] = "keyboardButtonTypeRequestLocation"

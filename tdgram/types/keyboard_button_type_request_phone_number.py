from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class KeyboardButtonTypeRequestPhoneNumber(BaseType):
    """
    A button that sends the user's phone number when pressed; available only in private chats
    """

    __type__: Literal["keyboardButtonTypeRequestPhoneNumber"] = (
        "keyboardButtonTypeRequestPhoneNumber"
    )

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarSharePhoneNumber(BaseType):
    """
    The chat is a private or secret chat with a mutual contact and the user's phone number can be shared with the other user using the method sharePhoneNumber
    """

    __type__: Literal["chatActionBarSharePhoneNumber"] = "chatActionBarSharePhoneNumber"

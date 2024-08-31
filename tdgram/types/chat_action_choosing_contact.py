from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionChoosingContact(BaseType):
    """
    The user is picking a contact to send
    """

    __type__: Literal["chatActionChoosingContact"] = "chatActionChoosingContact"

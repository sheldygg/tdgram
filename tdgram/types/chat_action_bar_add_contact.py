from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarAddContact(BaseType):
    """
    The chat is a private or secret chat and the other user can be added to the contact list using the method addContact
    """

    __type__: Literal["chatActionBarAddContact"] = "chatActionBarAddContact"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterContacts(BaseType):
    """
    Returns contacts of the user
    """

    __type__: Literal["chatMembersFilterContacts"] = "chatMembersFilterContacts"

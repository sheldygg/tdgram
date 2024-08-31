from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterBanned(BaseType):
    """
    Returns users banned from the chat; can be used only by administrators in a supergroup or in a channel
    """

    __type__: Literal["chatMembersFilterBanned"] = "chatMembersFilterBanned"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterBots(BaseType):
    """
    Returns bot members of the chat
    """

    __type__: Literal["chatMembersFilterBots"] = "chatMembersFilterBots"

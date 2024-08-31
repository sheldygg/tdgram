from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckChatUsernameResultPublicChatsTooMany(BaseType):
    """
    The user has too many chats with username, one of them must be made private first
    """

    __type__: Literal["checkChatUsernameResultPublicChatsTooMany"] = (
        "checkChatUsernameResultPublicChatsTooMany"
    )

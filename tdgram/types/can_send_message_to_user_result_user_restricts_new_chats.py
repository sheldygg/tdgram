from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendMessageToUserResultUserRestrictsNewChats(BaseType):
    """
    The user can't be messaged, because they restrict new chats with non-contacts
    """

    __type__: Literal["canSendMessageToUserResultUserRestrictsNewChats"] = (
        "canSendMessageToUserResultUserRestrictsNewChats"
    )

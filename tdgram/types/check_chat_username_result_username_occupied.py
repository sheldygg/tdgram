from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CheckChatUsernameResultUsernameOccupied(BaseType):
    """
    The username is occupied
    """

    __type__: Literal["checkChatUsernameResultUsernameOccupied"] = (
        "checkChatUsernameResultUsernameOccupied"
    )

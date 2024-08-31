from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SecretChatStatePending(BaseType):
    """
    The secret chat is not yet created; waiting for the other user to get online
    """

    __type__: Literal["secretChatStatePending"] = "secretChatStatePending"

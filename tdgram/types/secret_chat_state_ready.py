from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SecretChatStateReady(BaseType):
    """
    The secret chat is ready to use
    """

    __type__: Literal["secretChatStateReady"] = "secretChatStateReady"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SecretChatStateClosed(BaseType):
    """
    The secret chat is closed
    """

    __type__: Literal["secretChatStateClosed"] = "secretChatStateClosed"

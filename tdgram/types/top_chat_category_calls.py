from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryCalls(BaseType):
    """
    A category containing frequently used chats used for calls
    """

    __type__: Literal["topChatCategoryCalls"] = "topChatCategoryCalls"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryInlineBots(BaseType):
    """
    A category containing frequently used chats with inline bots sorted by their usage in inline mode
    """

    __type__: Literal["topChatCategoryInlineBots"] = "topChatCategoryInlineBots"

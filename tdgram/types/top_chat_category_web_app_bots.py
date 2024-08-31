from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryWebAppBots(BaseType):
    """
    A category containing frequently used chats with bots, which Web Apps were opened
    """

    __type__: Literal["topChatCategoryWebAppBots"] = "topChatCategoryWebAppBots"

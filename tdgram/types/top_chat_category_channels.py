from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryChannels(BaseType):
    """
    A category containing frequently used channels
    """

    __type__: Literal["topChatCategoryChannels"] = "topChatCategoryChannels"

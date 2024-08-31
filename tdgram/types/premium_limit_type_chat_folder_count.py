from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeChatFolderCount(BaseType):
    """
    The maximum number of chat folders
    """

    __type__: Literal["premiumLimitTypeChatFolderCount"] = "premiumLimitTypeChatFolderCount"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeShareableChatFolderCount(BaseType):
    """
    The maximum number of added shareable chat folders
    """

    __type__: Literal["premiumLimitTypeShareableChatFolderCount"] = (
        "premiumLimitTypeShareableChatFolderCount"
    )

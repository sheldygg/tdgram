from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TopChatCategoryGroups(BaseType):
    """
    A category containing frequently used basic groups and supergroups
    """

    __type__: Literal["topChatCategoryGroups"] = "topChatCategoryGroups"

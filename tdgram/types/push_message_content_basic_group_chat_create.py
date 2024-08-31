from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentBasicGroupChatCreate(BaseType):
    """
    A newly created basic group
    """

    __type__: Literal["pushMessageContentBasicGroupChatCreate"] = (
        "pushMessageContentBasicGroupChatCreate"
    )

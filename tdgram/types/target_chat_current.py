from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TargetChatCurrent(BaseType):
    """
    The currently opened chat needs to be kept
    """

    __type__: Literal["targetChatCurrent"] = "targetChatCurrent"

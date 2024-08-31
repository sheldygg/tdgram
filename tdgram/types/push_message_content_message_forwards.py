from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentMessageForwards(BaseType):
    """
    A forwarded messages
    """

    __type__: Literal["pushMessageContentMessageForwards"] = "pushMessageContentMessageForwards"

    total_count: int
    """Number of forwarded messages"""

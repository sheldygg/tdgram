from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Count(BaseType):
    """
    Contains a counter
    """

    __type__: Literal["count"] = "count"

    count: int
    """Count"""

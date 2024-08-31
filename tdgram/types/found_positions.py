from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FoundPositions(BaseType):
    """
    Contains 0-based positions of matched objects
    """

    __type__: Literal["foundPositions"] = "foundPositions"

    total_count: int
    """Total number of matched objects"""
    positions: list[int]
    """The positions of the matched objects"""

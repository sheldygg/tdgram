from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class FoundPosition(BaseType):
    """
    Contains 0-based match position
    """

    __type__: Literal["foundPosition"] = "foundPosition"

    position: int
    """The position of the match"""

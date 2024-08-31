from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Emojis(BaseType):
    """
    Represents a list of emojis
    """

    __type__: Literal["emojis"] = "emojis"

    emojis: list[str]
    """List of emojis"""

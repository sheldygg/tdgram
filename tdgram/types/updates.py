from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Update


@dataclass(kw_only=True)
class Updates(BaseType):
    """
    Contains a list of updates
    """

    __type__: Literal["updates"] = "updates"

    updates: list[Update]
    """List of updates"""

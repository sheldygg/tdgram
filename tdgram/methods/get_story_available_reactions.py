from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import AvailableReactions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStoryAvailableReactions(BaseMethod):
    """
    Returns reactions, which can be chosen for a story
    """

    __type__: Literal["getStoryAvailableReactions"] = "getStoryAvailableReactions"
    __returning_type__ = AvailableReactions

    row_size: int
    """Number of reaction per row, 5-25"""

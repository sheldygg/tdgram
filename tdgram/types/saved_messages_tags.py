from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import SavedMessagesTag


@dataclass(kw_only=True)
class SavedMessagesTags(BaseType):
    """
    Contains a list of tags used in Saved Messages
    """

    __type__: Literal["savedMessagesTags"] = "savedMessagesTags"

    tags: list[SavedMessagesTag]
    """List of tags"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateQuickReplyShortcuts(BaseType):
    """
    The list of quick reply shortcuts has changed
    """

    __type__: Literal["updateQuickReplyShortcuts"] = "updateQuickReplyShortcuts"

    shortcut_ids: list[int]
    """The new list of identifiers of quick reply shortcuts"""

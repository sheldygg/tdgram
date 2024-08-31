from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReorderQuickReplyShortcuts(BaseMethod):
    """
    Changes the order of quick reply shortcuts
    """

    __type__: Literal["reorderQuickReplyShortcuts"] = "reorderQuickReplyShortcuts"
    __returning_type__ = Ok

    shortcut_ids: list[int]
    """The new order of quick reply shortcuts"""

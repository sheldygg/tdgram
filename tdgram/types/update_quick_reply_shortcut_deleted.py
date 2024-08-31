from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateQuickReplyShortcutDeleted(BaseType):
    """
    A quick reply shortcut and all its messages were deleted
    """

    __type__: Literal["updateQuickReplyShortcutDeleted"] = "updateQuickReplyShortcutDeleted"

    shortcut_id: int
    """The identifier of the deleted shortcut"""

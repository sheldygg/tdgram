from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import QuickReplyShortcut


@dataclass(kw_only=True)
class UpdateQuickReplyShortcut(BaseType):
    """
    Basic information about a quick reply shortcut has changed. This update is guaranteed to come before the quick shortcut name is returned to the application
    """

    __type__: Literal["updateQuickReplyShortcut"] = "updateQuickReplyShortcut"

    shortcut: QuickReplyShortcut
    """New data about the shortcut"""

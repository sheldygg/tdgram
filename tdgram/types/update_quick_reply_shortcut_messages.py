from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import QuickReplyMessage


@dataclass(kw_only=True)
class UpdateQuickReplyShortcutMessages(BaseType):
    """
    The list of quick reply shortcut messages has changed
    """

    __type__: Literal["updateQuickReplyShortcutMessages"] = "updateQuickReplyShortcutMessages"

    shortcut_id: int
    """The identifier of the shortcut"""
    messages: list[QuickReplyMessage]
    """The new list of quick reply messages for the shortcut in order from the first to the last sent"""

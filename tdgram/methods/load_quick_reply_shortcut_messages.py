from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadQuickReplyShortcutMessages(BaseMethod):
    """
    Loads quick reply messages that can be sent by a given quick reply shortcut. The loaded messages will be sent through updateQuickReplyShortcutMessages
    """

    __type__: Literal["loadQuickReplyShortcutMessages"] = "loadQuickReplyShortcutMessages"
    __returning_type__ = Ok

    shortcut_id: int
    """Unique identifier of the quick reply shortcut"""

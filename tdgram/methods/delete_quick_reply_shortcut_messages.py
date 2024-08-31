from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteQuickReplyShortcutMessages(BaseMethod):
    """
    Deletes specified quick reply messages
    """

    __type__: Literal["deleteQuickReplyShortcutMessages"] = "deleteQuickReplyShortcutMessages"
    __returning_type__ = Ok

    shortcut_id: int
    """Unique identifier of the quick reply shortcut to which the messages belong"""
    message_ids: list[int]
    """Unique identifiers of the messages"""

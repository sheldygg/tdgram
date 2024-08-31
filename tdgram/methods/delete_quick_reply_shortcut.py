from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteQuickReplyShortcut(BaseMethod):
    """
    Deletes a quick reply shortcut
    """

    __type__: Literal["deleteQuickReplyShortcut"] = "deleteQuickReplyShortcut"
    __returning_type__ = Ok

    shortcut_id: int
    """Unique identifier of the quick reply shortcut"""

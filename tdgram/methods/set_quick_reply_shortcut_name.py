from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetQuickReplyShortcutName(BaseMethod):
    """
    Changes name of a quick reply shortcut
    """

    __type__: Literal["setQuickReplyShortcutName"] = "setQuickReplyShortcutName"
    __returning_type__ = Ok

    shortcut_id: int
    """Unique identifier of the quick reply shortcut"""
    name: str
    """New name for the shortcut. Use checkQuickReplyShortcutName to check its validness"""

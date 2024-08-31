from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckQuickReplyShortcutName(BaseMethod):
    """
    Checks validness of a name for a quick reply shortcut. Can be called synchronously
    """

    __type__: Literal["checkQuickReplyShortcutName"] = "checkQuickReplyShortcutName"
    __returning_type__ = Ok

    name: str
    """The name of the shortcut; 1-32 characters"""

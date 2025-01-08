from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadQuickReplyShortcuts(BaseMethod):
    """
    Loads quick reply shortcuts created by the current user. The loaded data will be sent through updateQuickReplyShortcut and updateQuickReplyShortcuts
    """

    __type__: Literal["loadQuickReplyShortcuts"] = "loadQuickReplyShortcuts"
    __returning_type__ = Ok

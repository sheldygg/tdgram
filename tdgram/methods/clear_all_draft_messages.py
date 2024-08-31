from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ClearAllDraftMessages(BaseMethod):
    """
    Clears message drafts in all chats
    """

    __type__: Literal["clearAllDraftMessages"] = "clearAllDraftMessages"
    __returning_type__ = Ok

    exclude_secret_chats: bool
    """Pass true to keep local message drafts in secret chats"""

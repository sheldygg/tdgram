from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleChatFolderTags(BaseMethod):
    """
    Toggles whether chat folder tags are enabled
    """

    __type__: Literal["toggleChatFolderTags"] = "toggleChatFolderTags"
    __returning_type__ = Ok

    are_tags_enabled: bool
    """Pass true to enable folder tags; pass false to disable them"""

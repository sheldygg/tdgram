from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ArchiveChatListSettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetArchiveChatListSettings(BaseMethod):
    """
    Changes settings for automatic moving of chats to and from the Archive chat lists
    """

    __type__: Literal["setArchiveChatListSettings"] = "setArchiveChatListSettings"
    __returning_type__ = Ok

    settings: ArchiveChatListSettings
    """New settings"""

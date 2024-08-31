from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ArchiveChatListSettings
from .base import BaseMethod


@dataclass(kw_only=True)
class GetArchiveChatListSettings(BaseMethod):
    """
    Returns settings for automatic moving of chats to and from the Archive chat lists
    """

    __type__: Literal["getArchiveChatListSettings"] = "getArchiveChatListSettings"
    __returning_type__ = ArchiveChatListSettings

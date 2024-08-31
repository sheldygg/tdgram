from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatFolderIcon(BaseType):
    """
    Represents an icon for a chat folder
    """

    __type__: Literal["chatFolderIcon"] = "chatFolderIcon"

    name: str
    """The chosen icon name for short folder representation; one of 'All', 'Unread', 'Unmuted', 'Bots', 'Channels', 'Groups', 'Private', 'Custom', 'Setup', 'Cat', 'Crown',"""

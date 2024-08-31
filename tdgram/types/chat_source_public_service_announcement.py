from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatSourcePublicServiceAnnouncement(BaseType):
    """
    The chat contains a public service announcement
    """

    __type__: Literal["chatSourcePublicServiceAnnouncement"] = (
        "chatSourcePublicServiceAnnouncement"
    )

    type: str
    """The type of the announcement"""
    text: str
    """The text of the announcement"""

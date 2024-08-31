from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageViewer(BaseType):
    """
    Represents a viewer of a message
    """

    __type__: Literal["messageViewer"] = "messageViewer"

    user_id: int
    """User identifier of the viewer"""
    view_date: int
    """Approximate point in time (Unix timestamp) when the message was viewed"""

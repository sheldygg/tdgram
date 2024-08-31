from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageViewer


@dataclass(kw_only=True)
class MessageViewers(BaseType):
    """
    Represents a list of message viewers
    """

    __type__: Literal["messageViewers"] = "messageViewers"

    viewers: list[MessageViewer]
    """List of message viewers"""

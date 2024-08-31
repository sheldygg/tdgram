from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import QuickReplyMessage


@dataclass(kw_only=True)
class QuickReplyShortcut(BaseType):
    """
    Describes a shortcut that can be used for a quick reply
    """

    __type__: Literal["quickReplyShortcut"] = "quickReplyShortcut"

    id: int
    """Unique shortcut identifier"""
    name: str
    """The name of the shortcut that can be used to use the shortcut"""
    first_message: QuickReplyMessage
    """The first shortcut message"""
    message_count: int
    """The total number of messages in the shortcut"""

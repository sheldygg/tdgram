from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class UpdateNewMessage(BaseType):
    """
    A new message was received; can also be an outgoing message
    """

    __type__: Literal["updateNewMessage"] = "updateNewMessage"

    message: Message
    """The new message"""

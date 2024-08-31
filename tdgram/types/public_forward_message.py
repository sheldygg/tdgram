from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class PublicForwardMessage(BaseType):
    """
    Contains a public forward as a message
    """

    __type__: Literal["publicForwardMessage"] = "publicForwardMessage"

    message: Message
    """Information about the message"""

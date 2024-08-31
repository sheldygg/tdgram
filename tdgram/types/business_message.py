from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class BusinessMessage(BaseType):
    """
    Describes a message from a business account as received by a bot
    """

    __type__: Literal["businessMessage"] = "businessMessage"

    message: Message
    """The message"""
    reply_to_message: Message | None = None
    """Message that is replied by the message in the same chat; may be null if none"""

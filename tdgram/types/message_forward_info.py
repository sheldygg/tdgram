from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForwardSource, MessageOrigin


@dataclass(kw_only=True)
class MessageForwardInfo(BaseType):
    """
    Contains information about a forwarded message
    """

    __type__: Literal["messageForwardInfo"] = "messageForwardInfo"

    origin: MessageOrigin
    """Origin of the forwarded message"""
    date: int
    """Point in time (Unix timestamp) when the message was originally sent"""
    source: ForwardSource | None = None
    """For messages forwarded to the chat with the current user (Saved Messages), to the Replies bot chat, or to the channel's discussion group, information about the source message from which the message was forwarded last time; may be null for other forwards or if unknown"""
    public_service_announcement_type: str
    """The type of public service announcement for the forwarded message"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageSender


@dataclass(kw_only=True)
class MessageSenders(BaseType):
    """
    Represents a list of message senders
    """

    __type__: Literal["messageSenders"] = "messageSenders"

    total_count: int
    """Approximate total number of messages senders found"""
    senders: list[MessageSender]
    """List of message senders"""

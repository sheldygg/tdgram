from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class ChatEventPollStopped(BaseType):
    """
    A poll in a message was stopped
    """

    __type__: Literal["chatEventPollStopped"] = "chatEventPollStopped"

    message: Message
    """The message with the poll"""

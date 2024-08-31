from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventShowMessageSenderToggled(BaseType):
    """
    The show_message_sender setting of a channel was toggled
    """

    __type__: Literal["chatEventShowMessageSenderToggled"] = "chatEventShowMessageSenderToggled"

    show_message_sender: bool
    """New value of show_message_sender"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventSignMessagesToggled(BaseType):
    """
    The sign_messages setting of a channel was toggled
    """

    __type__: Literal["chatEventSignMessagesToggled"] = "chatEventSignMessagesToggled"

    sign_messages: bool
    """New value of sign_messages"""

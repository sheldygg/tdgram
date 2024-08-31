from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TogglePaidMessageReactionIsAnonymous(BaseMethod):
    """
    Changes whether the paid message reaction of the user to a message is anonymous. The message must have paid reaction added by the user
    """

    __type__: Literal["togglePaidMessageReactionIsAnonymous"] = (
        "togglePaidMessageReactionIsAnonymous"
    )
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    is_anonymous: bool
    """Pass true to make paid reaction of the user on the message anonymous; pass false to make the user's profile visible among top reactors"""

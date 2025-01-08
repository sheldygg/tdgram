from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PreparedInlineMessage
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPreparedInlineMessage(BaseMethod):
    """
    Saves an inline message to be sent by the given user
    """

    __type__: Literal["getPreparedInlineMessage"] = "getPreparedInlineMessage"
    __returning_type__ = PreparedInlineMessage

    bot_user_id: int
    """Identifier of the bot that created the message"""
    prepared_message_id: str
    """Identifier of the prepared message"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputTextQuote


@dataclass(kw_only=True)
class InputMessageReplyToMessage(BaseType):
    """
    Describes a message to be replied in the same chat and forum topic
    """

    __type__: Literal["inputMessageReplyToMessage"] = "inputMessageReplyToMessage"

    message_id: int
    """The identifier of the message to be replied in the same chat and forum topic. A message can be replied in the same chat and forum topic only if messageProperties.can_be_replied"""
    quote: InputTextQuote | None = None
    """Quote from the message to be replied; pass null if none. Must always be null for replies in secret chats"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageInteractionInfo


@dataclass(kw_only=True)
class UpdateMessageInteractionInfo(BaseType):
    """
    The information about interactions with a message has changed
    """

    __type__: Literal["updateMessageInteractionInfo"] = "updateMessageInteractionInfo"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    interaction_info: MessageInteractionInfo | None = None
    """New information about interactions with the message; may be null"""

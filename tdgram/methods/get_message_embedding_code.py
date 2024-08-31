from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageEmbeddingCode(BaseMethod):
    """
    Returns an HTML code for embedding the message. Available only if messageProperties.can_get_embedding_code
    """

    __type__: Literal["getMessageEmbeddingCode"] = "getMessageEmbeddingCode"
    __returning_type__ = Text

    chat_id: int
    """Identifier of the chat to which the message belongs"""
    message_id: int
    """Identifier of the message"""
    for_album: bool
    """Pass true to return an HTML code for embedding of the whole media album"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PublicForwards
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessagePublicForwards(BaseMethod):
    """
    Returns forwarded copies of a channel message to different public channels and public reposts as a story. Can be used only if messageProperties.can_get_statistics == true. For optimal performance, the number of returned messages and stories is chosen by TDLib
    """

    __type__: Literal["getMessagePublicForwards"] = "getMessagePublicForwards"
    __returning_type__ = PublicForwards

    chat_id: int
    """Chat identifier of the message"""
    message_id: int
    """Message identifier"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit"""

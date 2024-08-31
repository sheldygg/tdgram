from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageThreadInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetMessageThread(BaseMethod):
    """
    Returns information about a message thread. Can be used only if messageProperties.can_get_message_thread == true
    """

    __type__: Literal["getMessageThread"] = "getMessageThread"
    __returning_type__ = MessageThreadInfo

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Identifier of the message"""

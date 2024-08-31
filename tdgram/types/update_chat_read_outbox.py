from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatReadOutbox(BaseType):
    """
    Outgoing messages were read
    """

    __type__: Literal["updateChatReadOutbox"] = "updateChatReadOutbox"

    chat_id: int
    """Chat identifier"""
    last_read_outbox_message_id: int
    """Identifier of last read outgoing message"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import DraftMessage, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatDraftMessage(BaseMethod):
    """
    Changes the draft message in a chat
    """

    __type__: Literal["setChatDraftMessage"] = "setChatDraftMessage"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """If not 0, the message thread identifier in which the draft was changed"""
    draft_message: DraftMessage | None = None
    """New draft message; pass null to remove the draft. All files in draft message content must be of the type inputFileLocal. Media thumbnails and captions are ignored"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageSchedulingState, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditMessageSchedulingState(BaseMethod):
    """
    Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
    """

    __type__: Literal["editMessageSchedulingState"] = "editMessageSchedulingState"
    __returning_type__ = Ok

    chat_id: int
    """The chat the message belongs to"""
    message_id: int
    """Identifier of the message. Use messageProperties.can_edit_scheduling_state to check whether the message is suitable"""
    scheduling_state: MessageSchedulingState | None = None
    """The new message scheduling state; pass null to send the message immediately. Must be null for messages in the state messageSchedulingStateSendWhenVideoProcessed"""

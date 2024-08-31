from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Error


@dataclass(kw_only=True)
class MessageSendingStateFailed(BaseType):
    """
    The message failed to be sent
    """

    __type__: Literal["messageSendingStateFailed"] = "messageSendingStateFailed"

    error: Error
    """The cause of the message sending failure"""
    can_retry: bool
    """True, if the message can be re-sent using resendMessages or readdQuickReplyShortcutMessages"""
    need_another_sender: bool
    """True, if the message can be re-sent only on behalf of a different sender"""
    need_another_reply_quote: bool
    """True, if the message can be re-sent only if another quote is chosen in the message that is replied by the given message"""
    need_drop_reply: bool
    """True, if the message can be re-sent only if the message to be replied is removed. This will be done automatically by resendMessages"""
    retry_after: float
    """Time left before the message can be re-sent, in seconds. No update is sent when this field changes"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReplyMarkupRemoveKeyboard(BaseType):
    """
    Instructs application to remove the keyboard once this message has been received. This kind of keyboard can't be received in an incoming message; instead, updateChatReplyMarkup with message_id == 0 will be sent
    """

    __type__: Literal["replyMarkupRemoveKeyboard"] = "replyMarkupRemoveKeyboard"

    is_personal: bool
    """True, if the keyboard is removed only for the mentioned users or the target user of a reply"""

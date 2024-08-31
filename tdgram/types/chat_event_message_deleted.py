from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class ChatEventMessageDeleted(BaseType):
    """
    A message was deleted
    """

    __type__: Literal["chatEventMessageDeleted"] = "chatEventMessageDeleted"

    message: Message
    """Deleted message"""
    can_report_anti_spam_false_positive: bool
    """True, if the message deletion can be reported via reportSupergroupAntiSpamFalsePositive"""

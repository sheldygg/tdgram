from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportSupergroupAntiSpamFalsePositive(BaseMethod):
    """
    Reports a false deletion of a message by aggressive anti-spam checks; requires administrator rights in the supergroup. Can be called only for messages from chatEventMessageDeleted with can_report_anti_spam_false_positive == true
    """

    __type__: Literal["reportSupergroupAntiSpamFalsePositive"] = (
        "reportSupergroupAntiSpamFalsePositive"
    )
    __returning_type__ = Ok

    supergroup_id: int
    """Supergroup identifier"""
    message_id: int
    """Identifier of the erroneously deleted message from chatEventMessageDeleted"""

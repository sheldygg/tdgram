from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReportSupergroupSpam(BaseMethod):
    """
    Reports messages in a supergroup as spam; requires administrator rights in the supergroup
    """

    __type__: Literal["reportSupergroupSpam"] = "reportSupergroupSpam"
    __returning_type__ = Ok

    supergroup_id: int
    """Supergroup identifier"""
    message_ids: list[int]
    """Identifiers of messages to report. Use messageProperties.can_report_supergroup_spam to check whether the message can be reported"""

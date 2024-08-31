from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessAwayMessageSchedule, BusinessRecipients


@dataclass(kw_only=True)
class BusinessAwayMessageSettings(BaseType):
    """
    Describes settings for messages that are automatically sent by a Telegram Business account when it is away
    """

    __type__: Literal["businessAwayMessageSettings"] = "businessAwayMessageSettings"

    shortcut_id: int
    """Unique quick reply shortcut identifier for the away messages"""
    recipients: BusinessRecipients
    """Chosen recipients of the away messages"""
    schedule: BusinessAwayMessageSchedule
    """Settings used to check whether the current user is away"""
    offline_only: bool
    """True, if the messages must not be sent if the account was online in the last 10 minutes"""

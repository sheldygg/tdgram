from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessGreetingMessageSettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessGreetingMessageSettings(BaseMethod):
    """
    Changes the business greeting message settings of the current user. Requires Telegram Business subscription
    """

    __type__: Literal["setBusinessGreetingMessageSettings"] = "setBusinessGreetingMessageSettings"
    __returning_type__ = Ok

    greeting_message_settings: BusinessGreetingMessageSettings | None = None
    """The new settings for the greeting message of the business; pass null to disable the greeting message"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupCanHaveSponsoredMessages(BaseMethod):
    """
    Toggles whether sponsored messages are shown in the channel chat; requires owner privileges in the channel. The chat must have at least chatBoostFeatures.min_sponsored_message_disable_boost_level boost level to disable sponsored messages
    """

    __type__: Literal["toggleSupergroupCanHaveSponsoredMessages"] = (
        "toggleSupergroupCanHaveSponsoredMessages"
    )
    __returning_type__ = Ok

    supergroup_id: int
    """The identifier of the channel"""
    can_have_sponsored_messages: bool
    """The new value of can_have_sponsored_messages"""

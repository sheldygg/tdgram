from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupJoinToSendMessages(BaseMethod):
    """
    Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right
    """

    __type__: Literal["toggleSupergroupJoinToSendMessages"] = "toggleSupergroupJoinToSendMessages"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup that isn't a broadcast group"""
    join_to_send_messages: bool
    """New value of join_to_send_messages"""

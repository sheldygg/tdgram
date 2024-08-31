from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSupergroupSignMessages(BaseMethod):
    """
    Toggles whether sender signature or link to the account is added to sent messages in a channel; requires can_change_info member right
    """

    __type__: Literal["toggleSupergroupSignMessages"] = "toggleSupergroupSignMessages"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the channel"""
    sign_messages: bool
    """New value of sign_messages"""
    show_message_sender: bool
    """New value of show_message_sender"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ShareUsersWithBot(BaseMethod):
    """
    Shares users after pressing a keyboardButtonTypeRequestUsers button with the bot
    """

    __type__: Literal["shareUsersWithBot"] = "shareUsersWithBot"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat with the bot"""
    message_id: int
    """Identifier of the message with the button"""
    button_id: int
    """Identifier of the button"""
    shared_user_ids: list[int]
    """Identifiers of the shared users"""
    only_check: bool
    """Pass true to check that the users can be shared by the button instead of actually sharing them"""

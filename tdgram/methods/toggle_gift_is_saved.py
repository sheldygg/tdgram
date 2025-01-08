from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGiftIsSaved(BaseMethod):
    """
    Toggles whether a gift is shown on the current user's profile page
    """

    __type__: Literal["toggleGiftIsSaved"] = "toggleGiftIsSaved"
    __returning_type__ = Ok

    sender_user_id: int
    """Identifier of the user that sent the gift"""
    message_id: int
    """Identifier of the message with the gift in the chat with the user"""
    is_saved: bool
    """Pass true to display the gift on the user's profile page; pass false to remove it from the profile page"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat, ChatLocation
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateNewSupergroupChat(BaseMethod):
    """
    Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
    """

    __type__: Literal["createNewSupergroupChat"] = "createNewSupergroupChat"
    __returning_type__ = Chat

    title: str
    """Title of the new chat; 1-128 characters"""
    is_forum: bool
    """Pass true to create a forum supergroup chat"""
    is_channel: bool
    """Pass true to create a channel chat; ignored if a forum is created"""
    description: str
    """Chat description; 0-255 characters"""
    location: ChatLocation | None = None
    """Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat"""
    message_auto_delete_time: int
    """Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically"""
    for_import: bool
    """Pass true to create a supergroup for importing messages using importMessages"""

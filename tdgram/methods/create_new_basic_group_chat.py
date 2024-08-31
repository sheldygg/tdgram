from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CreatedBasicGroupChat
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateNewBasicGroupChat(BaseMethod):
    """
    Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns information about the newly created chat
    """

    __type__: Literal["createNewBasicGroupChat"] = "createNewBasicGroupChat"
    __returning_type__ = CreatedBasicGroupChat

    user_ids: list[int] | None = None
    """Identifiers of users to be added to the basic group; may be empty to create a basic group without other members"""
    title: str
    """Title of the new basic group; 1-128 characters"""
    message_auto_delete_time: int
    """Message auto-delete time value, in seconds; must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically"""

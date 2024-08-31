from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleGeneralForumTopicIsHidden(BaseMethod):
    """
    Toggles whether a General topic is hidden in a forum supergroup chat; requires can_manage_topics right in the supergroup
    """

    __type__: Literal["toggleGeneralForumTopicIsHidden"] = "toggleGeneralForumTopicIsHidden"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    is_hidden: bool
    """Pass true to hide and close the General topic; pass false to unhide it"""

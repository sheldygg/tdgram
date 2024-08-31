from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageForumTopicEdited(BaseType):
    """
    A forum topic has been edited
    """

    __type__: Literal["messageForumTopicEdited"] = "messageForumTopicEdited"

    name: str | None = None
    """If non-empty, the new name of the topic"""
    edit_icon_custom_emoji_id: bool
    """True, if icon's custom_emoji_id is changed"""
    icon_custom_emoji_id: int
    """New unique identifier of the custom emoji shown on the topic icon; 0 if none. Must be ignored if edit_icon_custom_emoji_id is false"""

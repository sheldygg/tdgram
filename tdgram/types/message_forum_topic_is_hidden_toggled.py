from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageForumTopicIsHiddenToggled(BaseType):
    """
    A General forum topic has been hidden or unhidden
    """

    __type__: Literal["messageForumTopicIsHiddenToggled"] = "messageForumTopicIsHiddenToggled"

    is_hidden: bool
    """True, if the topic was hidden; otherwise, the topic was unhidden"""

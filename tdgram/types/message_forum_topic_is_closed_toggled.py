from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageForumTopicIsClosedToggled(BaseType):
    """
    A forum topic has been closed or opened
    """

    __type__: Literal["messageForumTopicIsClosedToggled"] = "messageForumTopicIsClosedToggled"

    is_closed: bool
    """True, if the topic was closed; otherwise, the topic was reopened"""

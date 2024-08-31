from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventIsForumToggled(BaseType):
    """
    The is_forum setting of a channel was toggled
    """

    __type__: Literal["chatEventIsForumToggled"] = "chatEventIsForumToggled"

    is_forum: bool
    """New value of is_forum"""

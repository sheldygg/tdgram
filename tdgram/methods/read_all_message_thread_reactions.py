from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReadAllMessageThreadReactions(BaseMethod):
    """
    Marks all reactions in a forum topic as read
    """

    __type__: Literal["readAllMessageThreadReactions"] = "readAllMessageThreadReactions"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """Message thread identifier in which reactions are marked as read"""

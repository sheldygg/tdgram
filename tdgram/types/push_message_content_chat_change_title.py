from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatChangeTitle(BaseType):
    """
    A chat title was edited
    """

    __type__: Literal["pushMessageContentChatChangeTitle"] = "pushMessageContentChatChangeTitle"

    title: str
    """New chat title"""

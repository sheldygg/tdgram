from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatSetBackground(BaseType):
    """
    A chat background was edited
    """

    __type__: Literal["pushMessageContentChatSetBackground"] = (
        "pushMessageContentChatSetBackground"
    )

    is_same: bool
    """True, if the set background is the same as the background of the current user"""

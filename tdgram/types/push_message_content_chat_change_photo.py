from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatChangePhoto(BaseType):
    """
    A chat photo was edited
    """

    __type__: Literal["pushMessageContentChatChangePhoto"] = "pushMessageContentChatChangePhoto"

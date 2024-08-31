from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendStoryResultBoostNeeded(BaseType):
    """
    The chat must be boosted first by Telegram Premium subscribers to post more stories. Call getChatBoostStatus to get current boost status of the chat
    """

    __type__: Literal["canSendStoryResultBoostNeeded"] = "canSendStoryResultBoostNeeded"

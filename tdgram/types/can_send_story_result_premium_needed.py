from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendStoryResultPremiumNeeded(BaseType):
    """
    The user must subscribe to Telegram Premium to be able to post stories
    """

    __type__: Literal["canSendStoryResultPremiumNeeded"] = "canSendStoryResultPremiumNeeded"

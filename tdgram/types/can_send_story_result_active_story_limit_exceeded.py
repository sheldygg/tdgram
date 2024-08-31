from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendStoryResultActiveStoryLimitExceeded(BaseType):
    """
    The limit for the number of active stories exceeded. The user can buy Telegram Premium, delete an active story, or wait for the oldest story to expire
    """

    __type__: Literal["canSendStoryResultActiveStoryLimitExceeded"] = (
        "canSendStoryResultActiveStoryLimitExceeded"
    )

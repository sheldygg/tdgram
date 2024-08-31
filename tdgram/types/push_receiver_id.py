from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushReceiverId(BaseType):
    """
    Contains a globally unique push receiver identifier, which can be used to identify which account has received a push notification
    """

    __type__: Literal["pushReceiverId"] = "pushReceiverId"

    id: int
    """The globally unique identifier of push notification subscription"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceNotification(BaseType):
    """
    The message is from a notification
    """

    __type__: Literal["messageSourceNotification"] = "messageSourceNotification"

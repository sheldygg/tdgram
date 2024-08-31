from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageExpiredVideo(BaseType):
    """
    A self-destructed video message
    """

    __type__: Literal["messageExpiredVideo"] = "messageExpiredVideo"

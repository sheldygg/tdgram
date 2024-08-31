from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageExpiredPhoto(BaseType):
    """
    A self-destructed photo message
    """

    __type__: Literal["messageExpiredPhoto"] = "messageExpiredPhoto"

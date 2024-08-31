from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReadDateTooOld(BaseType):
    """
    The message is too old to get read date
    """

    __type__: Literal["messageReadDateTooOld"] = "messageReadDateTooOld"

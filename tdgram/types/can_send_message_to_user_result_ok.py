from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendMessageToUserResultOk(BaseType):
    """
    The user can be messaged
    """

    __type__: Literal["canSendMessageToUserResultOk"] = "canSendMessageToUserResultOk"

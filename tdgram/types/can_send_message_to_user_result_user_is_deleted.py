from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CanSendMessageToUserResultUserIsDeleted(BaseType):
    """
    The user can't be messaged, because they are deleted or unknown
    """

    __type__: Literal["canSendMessageToUserResultUserIsDeleted"] = (
        "canSendMessageToUserResultUserIsDeleted"
    )

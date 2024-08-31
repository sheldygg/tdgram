from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSourceMessageThreadHistory(BaseType):
    """
    The message is from a message thread history
    """

    __type__: Literal["messageSourceMessageThreadHistory"] = "messageSourceMessageThreadHistory"

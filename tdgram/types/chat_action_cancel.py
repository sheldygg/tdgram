from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionCancel(BaseType):
    """
    The user has canceled the previous action
    """

    __type__: Literal["chatActionCancel"] = "chatActionCancel"

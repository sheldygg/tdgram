from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSelfDestructTypeImmediately(BaseType):
    """
    The message can be opened only once and will be self-destructed once closed
    """

    __type__: Literal["messageSelfDestructTypeImmediately"] = "messageSelfDestructTypeImmediately"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessFeatureBots(BaseType):
    """
    The ability to connect a bot to the account
    """

    __type__: Literal["businessFeatureBots"] = "businessFeatureBots"

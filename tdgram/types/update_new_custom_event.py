from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateNewCustomEvent(BaseType):
    """
    A new incoming event; for bots only
    """

    __type__: Literal["updateNewCustomEvent"] = "updateNewCustomEvent"

    event: str
    """A JSON-serialized event"""

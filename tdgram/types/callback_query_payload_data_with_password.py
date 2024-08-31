from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallbackQueryPayloadDataWithPassword(BaseType):
    """
    The payload for a callback button requiring password
    """

    __type__: Literal["callbackQueryPayloadDataWithPassword"] = (
        "callbackQueryPayloadDataWithPassword"
    )

    password: str
    """The 2-step verification password for the current user"""
    data: bytes
    """Data that was attached to the callback button"""

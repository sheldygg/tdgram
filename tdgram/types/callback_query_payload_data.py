from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CallbackQueryPayloadData(BaseType):
    """
    The payload for a general callback button
    """

    __type__: Literal["callbackQueryPayloadData"] = "callbackQueryPayloadData"

    data: bytes
    """Data that was attached to the callback button"""

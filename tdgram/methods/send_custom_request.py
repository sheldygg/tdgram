from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CustomRequestResult
from .base import BaseMethod


@dataclass(kw_only=True)
class SendCustomRequest(BaseMethod):
    """
    Sends a custom request; for bots only
    """

    __type__: Literal["sendCustomRequest"] = "sendCustomRequest"
    __returning_type__ = CustomRequestResult

    method: str
    """The method name"""
    parameters: str
    """JSON-serialized method parameters"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestBytes
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallBytes(BaseMethod):
    """
    Returns the received bytes; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallBytes"] = "testCallBytes"
    __returning_type__ = TestBytes

    x: bytes
    """Bytes to return"""

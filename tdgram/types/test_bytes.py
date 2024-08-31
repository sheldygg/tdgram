from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TestBytes(BaseType):
    """
    A simple object containing a sequence of bytes; for testing only
    """

    __type__: Literal["testBytes"] = "testBytes"

    value: bytes
    """Bytes"""

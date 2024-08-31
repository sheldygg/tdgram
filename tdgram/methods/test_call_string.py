from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TestString
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallString(BaseMethod):
    """
    Returns the received string; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallString"] = "testCallString"
    __returning_type__ = TestString

    x: str
    """String to return"""

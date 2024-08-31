from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TestGetDifference(BaseMethod):
    """
    Forces an updates.getDifference call to the Telegram servers; for testing only
    """

    __type__: Literal["testGetDifference"] = "testGetDifference"
    __returning_type__ = Ok

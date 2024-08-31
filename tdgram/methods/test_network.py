from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TestNetwork(BaseMethod):
    """
    Sends a simple network request to the Telegram servers; for testing only. Can be called before authorization
    """

    __type__: Literal["testNetwork"] = "testNetwork"
    __returning_type__ = Ok

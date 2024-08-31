from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Update
from .base import BaseMethod


@dataclass(kw_only=True)
class TestUseUpdate(BaseMethod):
    """
    Does nothing and ensures that the Update object is used; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testUseUpdate"] = "testUseUpdate"
    __returning_type__ = Update

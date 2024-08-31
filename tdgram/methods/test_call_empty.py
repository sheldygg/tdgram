from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class TestCallEmpty(BaseMethod):
    """
    Does nothing; for testing only. This is an offline method. Can be called before authorization
    """

    __type__: Literal["testCallEmpty"] = "testCallEmpty"
    __returning_type__ = Ok

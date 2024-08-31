from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LogStreamEmpty(BaseType):
    """
    The log is written nowhere
    """

    __type__: Literal["logStreamEmpty"] = "logStreamEmpty"

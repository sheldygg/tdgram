from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LogStreamDefault(BaseType):
    """
    The log is written to stderr or an OS specific log
    """

    __type__: Literal["logStreamDefault"] = "logStreamDefault"

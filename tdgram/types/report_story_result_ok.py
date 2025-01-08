from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportStoryResultOk(BaseType):
    """
    The story was reported successfully
    """

    __type__: Literal["reportStoryResultOk"] = "reportStoryResultOk"

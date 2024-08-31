from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonFake(BaseType):
    """
    The chat represents a fake account
    """

    __type__: Literal["reportReasonFake"] = "reportReasonFake"

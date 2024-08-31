from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonUnrelatedLocation(BaseType):
    """
    The location-based chat is unrelated to its stated location
    """

    __type__: Literal["reportReasonUnrelatedLocation"] = "reportReasonUnrelatedLocation"

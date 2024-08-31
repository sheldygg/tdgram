from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonPersonalDetails(BaseType):
    """
    The chat contains messages with personal details
    """

    __type__: Literal["reportReasonPersonalDetails"] = "reportReasonPersonalDetails"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonPornography(BaseType):
    """
    The chat contains pornographic messages
    """

    __type__: Literal["reportReasonPornography"] = "reportReasonPornography"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonSpam(BaseType):
    """
    The chat contains spam messages
    """

    __type__: Literal["reportReasonSpam"] = "reportReasonSpam"

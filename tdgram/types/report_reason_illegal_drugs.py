from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonIllegalDrugs(BaseType):
    """
    The chat has illegal drugs related content
    """

    __type__: Literal["reportReasonIllegalDrugs"] = "reportReasonIllegalDrugs"

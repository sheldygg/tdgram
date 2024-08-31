from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonChildAbuse(BaseType):
    """
    The chat has child abuse related content
    """

    __type__: Literal["reportReasonChildAbuse"] = "reportReasonChildAbuse"

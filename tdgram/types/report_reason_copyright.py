from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonCopyright(BaseType):
    """
    The chat contains copyrighted content
    """

    __type__: Literal["reportReasonCopyright"] = "reportReasonCopyright"

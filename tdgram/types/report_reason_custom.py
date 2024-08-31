from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ReportReasonCustom(BaseType):
    """
    A custom reason provided by the user
    """

    __type__: Literal["reportReasonCustom"] = "reportReasonCustom"

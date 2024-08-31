from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PaidMediaUnsupported(BaseType):
    """
    The media is unsupported
    """

    __type__: Literal["paidMediaUnsupported"] = "paidMediaUnsupported"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatActionBarReportUnrelatedLocation(BaseType):
    """
    The chat is a location-based supergroup, which can be reported as having unrelated location using the method reportChat with the reason reportReasonUnrelatedLocation
    """

    __type__: Literal["chatActionBarReportUnrelatedLocation"] = (
        "chatActionBarReportUnrelatedLocation"
    )

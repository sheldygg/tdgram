from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeRestorePurchases(BaseType):
    """
    The link forces restore of App Store purchases when opened. For official iOS application only
    """

    __type__: Literal["internalLinkTypeRestorePurchases"] = "internalLinkTypeRestorePurchases"

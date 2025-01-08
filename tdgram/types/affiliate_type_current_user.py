from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class AffiliateTypeCurrentUser(BaseType):
    """
    The affiliate is the current user
    """

    __type__: Literal["affiliateTypeCurrentUser"] = "affiliateTypeCurrentUser"

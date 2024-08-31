from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumFeatureIncreasedUploadFileSize(BaseType):
    """
    Increased maximum upload file size
    """

    __type__: Literal["premiumFeatureIncreasedUploadFileSize"] = (
        "premiumFeatureIncreasedUploadFileSize"
    )

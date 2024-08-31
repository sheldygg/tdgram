from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypePremiumGiftCode(BaseType):
    """
    The link is a link to a Telegram Premium gift code
    """

    __type__: Literal["linkPreviewTypePremiumGiftCode"] = "linkPreviewTypePremiumGiftCode"

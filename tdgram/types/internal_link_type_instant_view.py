from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeInstantView(BaseType):
    """
    The link must be opened in an Instant View. Call getWebPageInstantView with the given URL to process the link.
    """

    __type__: Literal["internalLinkTypeInstantView"] = "internalLinkTypeInstantView"

    url: str
    """URL to be passed to getWebPageInstantView"""
    fallback_url: str
    """An URL to open if getWebPageInstantView fails"""

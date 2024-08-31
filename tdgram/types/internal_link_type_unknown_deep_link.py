from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeUnknownDeepLink(BaseType):
    """
    The link is an unknown tg: link. Call getDeepLinkInfo to process the link
    """

    __type__: Literal["internalLinkTypeUnknownDeepLink"] = "internalLinkTypeUnknownDeepLink"

    link: str
    """Link to be passed to getDeepLinkInfo"""

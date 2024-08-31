from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TMeUrl


@dataclass(kw_only=True)
class TMeUrls(BaseType):
    """
    Contains a list of t.me URLs
    """

    __type__: Literal["tMeUrls"] = "tMeUrls"

    urls: list[TMeUrl]
    """List of URLs"""

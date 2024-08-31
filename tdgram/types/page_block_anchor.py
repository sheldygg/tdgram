from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockAnchor(BaseType):
    """
    An invisible anchor on a page, which can be used in a URL to open the page from the specified anchor
    """

    __type__: Literal["pageBlockAnchor"] = "pageBlockAnchor"

    name: str
    """Name of the anchor"""

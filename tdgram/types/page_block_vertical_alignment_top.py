from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockVerticalAlignmentTop(BaseType):
    """
    The content must be top-aligned
    """

    __type__: Literal["pageBlockVerticalAlignmentTop"] = "pageBlockVerticalAlignmentTop"

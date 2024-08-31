from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockVerticalAlignmentMiddle(BaseType):
    """
    The content must be middle-aligned
    """

    __type__: Literal["pageBlockVerticalAlignmentMiddle"] = "pageBlockVerticalAlignmentMiddle"

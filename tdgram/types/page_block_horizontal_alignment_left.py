from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockHorizontalAlignmentLeft(BaseType):
    """
    The content must be left-aligned
    """

    __type__: Literal["pageBlockHorizontalAlignmentLeft"] = "pageBlockHorizontalAlignmentLeft"

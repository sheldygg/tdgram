from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockHorizontalAlignmentCenter(BaseType):
    """
    The content must be center-aligned
    """

    __type__: Literal["pageBlockHorizontalAlignmentCenter"] = "pageBlockHorizontalAlignmentCenter"

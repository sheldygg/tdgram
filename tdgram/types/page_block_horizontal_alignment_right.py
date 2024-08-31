from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockHorizontalAlignmentRight(BaseType):
    """
    The content must be right-aligned
    """

    __type__: Literal["pageBlockHorizontalAlignmentRight"] = "pageBlockHorizontalAlignmentRight"

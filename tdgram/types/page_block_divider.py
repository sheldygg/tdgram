from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PageBlockDivider(BaseType):
    """
    An empty block separating a page
    """

    __type__: Literal["pageBlockDivider"] = "pageBlockDivider"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BlockListStories(BaseType):
    """
    The block list that disallows viewing of stories of the current user
    """

    __type__: Literal["blockListStories"] = "blockListStories"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterAnimation(BaseType):
    """
    Returns only animation messages
    """

    __type__: Literal["searchMessagesFilterAnimation"] = "searchMessagesFilterAnimation"

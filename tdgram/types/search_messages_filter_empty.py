from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SearchMessagesFilterEmpty(BaseType):
    """
    Returns all found messages, no filter is applied
    """

    __type__: Literal["searchMessagesFilterEmpty"] = "searchMessagesFilterEmpty"

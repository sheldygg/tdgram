from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputStoryAreaTypeLink(BaseType):
    """
    An area pointing to a HTTP or tg:// link
    """

    __type__: Literal["inputStoryAreaTypeLink"] = "inputStoryAreaTypeLink"

    url: str
    """HTTP or tg:// URL to be opened when the area is clicked"""

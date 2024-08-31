from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Hashtags(BaseType):
    """
    Contains a list of hashtags
    """

    __type__: Literal["hashtags"] = "hashtags"

    hashtags: list[str]
    """A list of hashtags"""

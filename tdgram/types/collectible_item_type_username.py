from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class CollectibleItemTypeUsername(BaseType):
    """
    A username
    """

    __type__: Literal["collectibleItemTypeUsername"] = "collectibleItemTypeUsername"

    username: str
    """The username"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LogTags(BaseType):
    """
    Contains a list of available TDLib internal log tags
    """

    __type__: Literal["logTags"] = "logTags"

    tags: list[str]
    """List of log tags"""

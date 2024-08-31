from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GroupCallVideoQualityThumbnail(BaseType):
    """
    The worst available video quality
    """

    __type__: Literal["groupCallVideoQualityThumbnail"] = "groupCallVideoQualityThumbnail"

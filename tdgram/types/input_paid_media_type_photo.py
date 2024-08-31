from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InputPaidMediaTypePhoto(BaseType):
    """
    The media is a photo. The photo must be at most 10 MB in size. The photo's width and height must not exceed 10000 in total. Width and height ratio must be at most 20
    """

    __type__: Literal["inputPaidMediaTypePhoto"] = "inputPaidMediaTypePhoto"

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeCode(BaseType):
    """
    Text that must be formatted as if inside a code HTML tag
    """

    __type__: Literal["textEntityTypeCode"] = "textEntityTypeCode"

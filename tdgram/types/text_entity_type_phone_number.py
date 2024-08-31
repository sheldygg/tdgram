from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypePhoneNumber(BaseType):
    """
    A phone number
    """

    __type__: Literal["textEntityTypePhoneNumber"] = "textEntityTypePhoneNumber"

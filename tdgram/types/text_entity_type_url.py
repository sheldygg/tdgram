from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TextEntityTypeUrl(BaseType):
    """
    An HTTP URL
    """

    __type__: Literal["textEntityTypeUrl"] = "textEntityTypeUrl"

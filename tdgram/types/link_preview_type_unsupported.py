from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LinkPreviewTypeUnsupported(BaseType):
    """
    The link preview type is unsupported yet
    """

    __type__: Literal["linkPreviewTypeUnsupported"] = "linkPreviewTypeUnsupported"

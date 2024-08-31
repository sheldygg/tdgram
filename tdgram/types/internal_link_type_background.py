from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeBackground(BaseType):
    """
    The link is a link to a background. Call searchBackground with the given background name to process the link
    """

    __type__: Literal["internalLinkTypeBackground"] = "internalLinkTypeBackground"

    background_name: str
    """Name of the background"""

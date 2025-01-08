from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Gifts
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAvailableGifts(BaseMethod):
    """
    Returns gifts that can be sent to other users
    """

    __type__: Literal["getAvailableGifts"] = "getAvailableGifts"
    __returning_type__ = Gifts

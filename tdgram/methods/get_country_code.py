from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCountryCode(BaseMethod):
    """
    Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization
    """

    __type__: Literal["getCountryCode"] = "getCountryCode"
    __returning_type__ = Text

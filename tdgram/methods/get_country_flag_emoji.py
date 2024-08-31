from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCountryFlagEmoji(BaseMethod):
    """
    Returns an emoji for the given country. Returns an empty string on failure. Can be called synchronously
    """

    __type__: Literal["getCountryFlagEmoji"] = "getCountryFlagEmoji"
    __returning_type__ = Text

    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code as received from getCountries"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPreferredCountryLanguage(BaseMethod):
    """
    Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown
    """

    __type__: Literal["getPreferredCountryLanguage"] = "getPreferredCountryLanguage"
    __returning_type__ = Text

    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code"""

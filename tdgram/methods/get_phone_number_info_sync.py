from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PhoneNumberInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPhoneNumberInfoSync(BaseMethod):
    """
    Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously
    """

    __type__: Literal["getPhoneNumberInfoSync"] = "getPhoneNumberInfoSync"
    __returning_type__ = PhoneNumberInfo

    language_code: str
    """A two-letter ISO 639-1 language code for country information localization"""
    phone_number_prefix: str
    """The phone number prefix"""

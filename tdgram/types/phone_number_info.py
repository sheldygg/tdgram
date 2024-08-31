from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import CountryInfo


@dataclass(kw_only=True)
class PhoneNumberInfo(BaseType):
    """
    Contains information about a phone number
    """

    __type__: Literal["phoneNumberInfo"] = "phoneNumberInfo"

    country: CountryInfo | None = None
    """Information about the country to which the phone number belongs; may be null"""
    country_calling_code: str
    """The part of the phone number denoting country calling code or its part"""
    formatted_phone_number: str
    """The phone number without country calling code formatted accordingly to local rules. Expected digits are returned as '-', but even more digits might be entered by the user"""
    is_anonymous: bool
    """True, if the phone number was bought at https://fragment.com and isn't tied to a SIM card. Information about the phone number can be received using getCollectibleItemInfo"""

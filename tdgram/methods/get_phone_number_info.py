from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PhoneNumberInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPhoneNumberInfo(BaseMethod):
    """
    Returns information about a phone number by its prefix. Can be called before authorization
    """

    __type__: Literal["getPhoneNumberInfo"] = "getPhoneNumberInfo"
    __returning_type__ = PhoneNumberInfo

    phone_number_prefix: str
    """The phone number prefix"""

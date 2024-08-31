from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Date


@dataclass(kw_only=True)
class PersonalDetails(BaseType):
    """
    Contains the user's personal details
    """

    __type__: Literal["personalDetails"] = "personalDetails"

    first_name: str
    """First name of the user written in English; 1-255 characters"""
    middle_name: str
    """Middle name of the user written in English; 0-255 characters"""
    last_name: str
    """Last name of the user written in English; 1-255 characters"""
    native_first_name: str
    """Native first name of the user; 1-255 characters"""
    native_middle_name: str
    """Native middle name of the user; 0-255 characters"""
    native_last_name: str
    """Native last name of the user; 1-255 characters"""
    birthdate: Date
    """Birthdate of the user"""
    gender: str
    """Gender of the user, 'male' or 'female'"""
    country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code of the user's country"""
    residence_country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code of the user's residence country"""

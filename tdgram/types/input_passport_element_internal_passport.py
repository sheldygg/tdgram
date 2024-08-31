from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputIdentityDocument


@dataclass(kw_only=True)
class InputPassportElementInternalPassport(BaseType):
    """
    A Telegram Passport element to be saved containing the user's internal passport
    """

    __type__: Literal["inputPassportElementInternalPassport"] = (
        "inputPassportElementInternalPassport"
    )

    internal_passport: InputIdentityDocument
    """The internal passport to be saved"""

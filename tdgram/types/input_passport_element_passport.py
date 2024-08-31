from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputIdentityDocument


@dataclass(kw_only=True)
class InputPassportElementPassport(BaseType):
    """
    A Telegram Passport element to be saved containing the user's passport
    """

    __type__: Literal["inputPassportElementPassport"] = "inputPassportElementPassport"

    passport: InputIdentityDocument
    """The passport to be saved"""

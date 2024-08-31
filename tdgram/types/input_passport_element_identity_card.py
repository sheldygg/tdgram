from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputIdentityDocument


@dataclass(kw_only=True)
class InputPassportElementIdentityCard(BaseType):
    """
    A Telegram Passport element to be saved containing the user's identity card
    """

    __type__: Literal["inputPassportElementIdentityCard"] = "inputPassportElementIdentityCard"

    identity_card: InputIdentityDocument
    """The identity card to be saved"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputPassportElementError, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPassportElementErrors(BaseMethod):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed
    """

    __type__: Literal["setPassportElementErrors"] = "setPassportElementErrors"
    __returning_type__ = Ok

    user_id: int
    """User identifier"""
    errors: list[InputPassportElementError]
    """The errors"""

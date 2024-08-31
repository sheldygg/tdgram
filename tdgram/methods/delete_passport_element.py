from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PassportElementType
from .base import BaseMethod


@dataclass(kw_only=True)
class DeletePassportElement(BaseMethod):
    """
    Deletes a Telegram Passport element
    """

    __type__: Literal["deletePassportElement"] = "deletePassportElement"
    __returning_type__ = Ok

    type: PassportElementType
    """Element type"""

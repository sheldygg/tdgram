from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextPhoneNumber(BaseType):
    """
    A rich text phone number
    """

    __type__: Literal["richTextPhoneNumber"] = "richTextPhoneNumber"

    text: RichText
    """Text"""
    phone_number: str
    """Phone number"""

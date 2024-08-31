from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextEmailAddress(BaseType):
    """
    A rich text email link
    """

    __type__: Literal["richTextEmailAddress"] = "richTextEmailAddress"

    text: RichText
    """Text"""
    email_address: str
    """Email address"""

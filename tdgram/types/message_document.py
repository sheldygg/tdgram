from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document, FormattedText


@dataclass(kw_only=True)
class MessageDocument(BaseType):
    """
    A document message (general file)
    """

    __type__: Literal["messageDocument"] = "messageDocument"

    document: Document
    """The document description"""
    caption: FormattedText
    """Document caption"""

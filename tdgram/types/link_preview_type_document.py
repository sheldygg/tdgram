from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document


@dataclass(kw_only=True)
class LinkPreviewTypeDocument(BaseType):
    """
    The link is a link to a general file
    """

    __type__: Literal["linkPreviewTypeDocument"] = "linkPreviewTypeDocument"

    document: Document
    """The document description"""
    author: str
    """Author of the document"""

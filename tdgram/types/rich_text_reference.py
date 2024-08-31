from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextReference(BaseType):
    """
    A reference to a richTexts object on the same page
    """

    __type__: Literal["richTextReference"] = "richTextReference"

    text: RichText
    """The text"""
    anchor_name: str
    """The name of a richTextAnchor object, which is the first element of the target richTexts object"""
    url: str
    """An HTTP URL, opening the reference"""

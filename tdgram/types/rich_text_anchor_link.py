from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextAnchorLink(BaseType):
    """
    A link to an anchor on the same page
    """

    __type__: Literal["richTextAnchorLink"] = "richTextAnchorLink"

    text: RichText
    """The link text"""
    anchor_name: str
    """The anchor name. If the name is empty, the link must bring back to top"""
    url: str
    """An HTTP URL, opening the anchor"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class PageBlockCaption(BaseType):
    """
    Contains a caption of another block
    """

    __type__: Literal["pageBlockCaption"] = "pageBlockCaption"

    text: RichText
    """Content of the caption"""
    credit: RichText
    """Block credit (like HTML tag <cite>)"""

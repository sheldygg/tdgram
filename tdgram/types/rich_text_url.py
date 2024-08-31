from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import RichText


@dataclass(kw_only=True)
class RichTextUrl(BaseType):
    """
    A rich text URL link
    """

    __type__: Literal["richTextUrl"] = "richTextUrl"

    text: RichText
    """Text"""
    url: str
    """URL"""
    is_cached: bool
    """True, if the URL has cached instant view server-side"""

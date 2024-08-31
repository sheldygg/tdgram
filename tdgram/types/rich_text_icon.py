from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Document


@dataclass(kw_only=True)
class RichTextIcon(BaseType):
    """
    A small image inside the text
    """

    __type__: Literal["richTextIcon"] = "richTextIcon"

    document: Document
    """The image represented as a document. The image can be in GIF, JPEG or PNG format"""
    width: int
    """Width of a bounding box in which the image must be shown; 0 if unknown"""
    height: int
    """Height of a bounding box in which the image must be shown; 0 if unknown"""

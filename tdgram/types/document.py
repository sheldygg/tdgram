from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, Minithumbnail, Thumbnail


@dataclass(kw_only=True)
class Document(BaseType):
    """
    Describes a document of any type
    """

    __type__: Literal["document"] = "document"

    file_name: str
    """Original name of the file; as defined by the sender"""
    mime_type: str
    """MIME type of the file; as defined by the sender"""
    minithumbnail: Minithumbnail | None = None
    """Document minithumbnail; may be null"""
    thumbnail: Thumbnail | None = None
    """Document thumbnail in JPEG or PNG format (PNG will be used only for background patterns); as defined by the sender; may be null"""
    document: File
    """File containing the document"""

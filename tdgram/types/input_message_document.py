from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, InputFile, InputThumbnail


@dataclass(kw_only=True)
class InputMessageDocument(BaseType):
    """
    A document message (general file)
    """

    __type__: Literal["inputMessageDocument"] = "inputMessageDocument"

    document: InputFile
    """Document to be sent"""
    thumbnail: InputThumbnail | None = None
    """Document thumbnail; pass null to skip thumbnail uploading"""
    disable_content_type_detection: bool
    """Pass true to disable automatic file type detection and send the document as a file. Always true for files sent to secret chats"""
    caption: FormattedText | None = None
    """Document caption; pass null to use an empty caption; 0-getOption('message_caption_length_max') characters"""

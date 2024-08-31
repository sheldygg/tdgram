from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File, InputFile, StickerFormat
from .base import BaseMethod


@dataclass(kw_only=True)
class UploadStickerFile(BaseMethod):
    """
    Uploads a file with a sticker; returns the uploaded file
    """

    __type__: Literal["uploadStickerFile"] = "uploadStickerFile"
    __returning_type__ = File

    user_id: int
    """Sticker file owner; ignored for regular users"""
    sticker_format: StickerFormat
    """Sticker format"""
    sticker: InputFile
    """File file to upload; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side."""

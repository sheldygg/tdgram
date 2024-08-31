from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File, FileType, InputFile
from .base import BaseMethod


@dataclass(kw_only=True)
class PreliminaryUploadFile(BaseMethod):
    """
    Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes.
    """

    __type__: Literal["preliminaryUploadFile"] = "preliminaryUploadFile"
    __returning_type__ = File

    file: InputFile
    """File to upload"""
    file_type: FileType | None = None
    """File type; pass null if unknown"""
    priority: int
    """Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first"""

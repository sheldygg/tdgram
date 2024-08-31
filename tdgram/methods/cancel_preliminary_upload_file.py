from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class CancelPreliminaryUploadFile(BaseMethod):
    """
    Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile. For other files the behavior is undefined
    """

    __type__: Literal["cancelPreliminaryUploadFile"] = "cancelPreliminaryUploadFile"
    __returning_type__ = Ok

    file_id: int
    """Identifier of the file to stop uploading"""

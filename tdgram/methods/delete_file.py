from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteFile(BaseMethod):
    """
    Deletes a file from the TDLib file cache
    """

    __type__: Literal["deleteFile"] = "deleteFile"
    __returning_type__ = Ok

    file_id: int
    """Identifier of the file to delete"""

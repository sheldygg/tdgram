from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import File
from .base import BaseMethod


@dataclass(kw_only=True)
class GetFile(BaseMethod):
    """
    Returns information about a file; this is an offline request
    """

    __type__: Literal["getFile"] = "getFile"
    __returning_type__ = File

    file_id: int
    """Identifier of the file to get"""

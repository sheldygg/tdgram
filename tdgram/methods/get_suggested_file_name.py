from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Text
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSuggestedFileName(BaseMethod):
    """
    Returns suggested name for saving a file in a given directory
    """

    __type__: Literal["getSuggestedFileName"] = "getSuggestedFileName"
    __returning_type__ = Text

    file_id: int
    """Identifier of the file"""
    directory: str
    """Directory in which the file is supposed to be saved"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateFileGenerationStart(BaseType):
    """
    The file generation process needs to be started by the application
    """

    __type__: Literal["updateFileGenerationStart"] = "updateFileGenerationStart"

    generation_id: int
    """Unique identifier for the generation process"""
    original_path: str | None = None
    """The path to a file from which a new file is generated; may be empty"""
    destination_path: str
    """The path to a file that must be created and where the new file is generated"""
    conversion: str
    """String specifying the conversion applied to the original file. If conversion is '#url#' than original_path contains an HTTP/HTTPS URL of a file, which must be downloaded by the application"""

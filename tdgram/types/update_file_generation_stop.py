from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateFileGenerationStop(BaseType):
    """
    File generation is no longer needed
    """

    __type__: Literal["updateFileGenerationStop"] = "updateFileGenerationStop"

    generation_id: int
    """Unique identifier for the generation process"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetFileGenerationProgress(BaseMethod):
    """
    Informs TDLib on a file generation progress
    """

    __type__: Literal["setFileGenerationProgress"] = "setFileGenerationProgress"
    __returning_type__ = Ok

    generation_id: int
    """The identifier of the generation process"""
    expected_size: int
    """Expected size of the generated file, in bytes; 0 if unknown"""
    local_prefix_size: int
    """The number of bytes already generated"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Error, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class FinishFileGeneration(BaseMethod):
    """
    Finishes the file generation
    """

    __type__: Literal["finishFileGeneration"] = "finishFileGeneration"
    __returning_type__ = Ok

    generation_id: int
    """The identifier of the generation process"""
    error: Error | None = None
    """If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded"""

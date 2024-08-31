from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveSavedAnimation(BaseMethod):
    """
    Removes an animation from the list of saved animations
    """

    __type__: Literal["removeSavedAnimation"] = "removeSavedAnimation"
    __returning_type__ = Ok

    animation: InputFile
    """Animation file to be removed"""

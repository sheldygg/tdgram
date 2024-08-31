from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddSavedAnimation(BaseMethod):
    """
    Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first.
    """

    __type__: Literal["addSavedAnimation"] = "addSavedAnimation"
    __returning_type__ = Ok

    animation: InputFile
    """The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list"""

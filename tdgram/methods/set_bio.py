from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBio(BaseMethod):
    """
    Changes the bio of the current user
    """

    __type__: Literal["setBio"] = "setBio"
    __returning_type__ = Ok

    bio: str
    """The new value of the user bio; 0-getOption('bio_length_max') characters without line feeds"""

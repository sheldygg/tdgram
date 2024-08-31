from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteProfilePhoto(BaseMethod):
    """
    Deletes a profile photo
    """

    __type__: Literal["deleteProfilePhoto"] = "deleteProfilePhoto"
    __returning_type__ = Ok

    profile_photo_id: int
    """Identifier of the profile photo to delete"""

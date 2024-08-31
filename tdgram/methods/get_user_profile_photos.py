from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatPhotos
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserProfilePhotos(BaseMethod):
    """
    Returns the profile photos of a user. Personal and public photo aren't returned
    """

    __type__: Literal["getUserProfilePhotos"] = "getUserProfilePhotos"
    __returning_type__ = ChatPhotos

    user_id: int
    """User identifier"""
    offset: int
    """The number of photos to skip; must be non-negative"""
    limit: int
    """The maximum number of photos to be returned; up to 100"""

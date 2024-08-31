from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import UserLink
from .base import BaseMethod


@dataclass(kw_only=True)
class GetUserLink(BaseMethod):
    """
    Returns an HTTPS link, which can be used to get information about the current user
    """

    __type__: Literal["getUserLink"] = "getUserLink"
    __returning_type__ = UserLink

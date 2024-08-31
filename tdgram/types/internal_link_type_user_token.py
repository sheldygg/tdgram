from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeUserToken(BaseType):
    """
    The link is a link to a user by a temporary token. Call searchUserByToken with the given token to process the link.
    """

    __type__: Literal["internalLinkTypeUserToken"] = "internalLinkTypeUserToken"

    token: str
    """The token"""

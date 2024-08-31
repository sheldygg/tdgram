from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InternalLinkType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInternalLinkType(BaseMethod):
    """
    Returns information about the type of internal link. Returns a 404 error if the link is not internal. Can be called before authorization
    """

    __type__: Literal["getInternalLinkType"] = "getInternalLinkType"
    __returning_type__ = InternalLinkType

    link: str
    """The link"""

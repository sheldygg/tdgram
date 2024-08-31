from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class LoginUrlInfoOpen(BaseType):
    """
    An HTTP URL needs to be open
    """

    __type__: Literal["loginUrlInfoOpen"] = "loginUrlInfoOpen"

    url: str
    """The URL to open"""
    skip_confirmation: bool
    """True, if there is no need to show an ordinary open URL confirmation"""

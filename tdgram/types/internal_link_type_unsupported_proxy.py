from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeUnsupportedProxy(BaseType):
    """
    The link is a link to an unsupported proxy. An alert can be shown to the user
    """

    __type__: Literal["internalLinkTypeUnsupportedProxy"] = "internalLinkTypeUnsupportedProxy"

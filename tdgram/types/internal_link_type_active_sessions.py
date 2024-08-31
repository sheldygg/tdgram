from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeActiveSessions(BaseType):
    """
    The link is a link to the Devices section of the application. Use getActiveSessions to get the list of active sessions and show them to the user
    """

    __type__: Literal["internalLinkTypeActiveSessions"] = "internalLinkTypeActiveSessions"

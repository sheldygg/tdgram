from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypeDefaultMessageAutoDeleteTimerSettings(BaseType):
    """
    The link is a link to the default message auto-delete timer settings section of the application settings
    """

    __type__: Literal["internalLinkTypeDefaultMessageAutoDeleteTimerSettings"] = (
        "internalLinkTypeDefaultMessageAutoDeleteTimerSettings"
    )

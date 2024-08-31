from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceUnspecified(BaseType):
    """
    The element contains an error in an unspecified place. The error will be considered resolved when new data is added
    """

    __type__: Literal["passportElementErrorSourceUnspecified"] = (
        "passportElementErrorSourceUnspecified"
    )

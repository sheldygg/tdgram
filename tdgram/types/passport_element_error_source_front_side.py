from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceFrontSide(BaseType):
    """
    The front side of the document contains an error. The error will be considered resolved when the file with the front side changes
    """

    __type__: Literal["passportElementErrorSourceFrontSide"] = (
        "passportElementErrorSourceFrontSide"
    )

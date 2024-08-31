from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PassportElementErrorSourceSelfie(BaseType):
    """
    The selfie with the document contains an error. The error will be considered resolved when the file with the selfie changes
    """

    __type__: Literal["passportElementErrorSourceSelfie"] = "passportElementErrorSourceSelfie"

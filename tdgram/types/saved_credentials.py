from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class SavedCredentials(BaseType):
    """
    Contains information about saved payment credentials
    """

    __type__: Literal["savedCredentials"] = "savedCredentials"

    id: str
    """Unique identifier of the saved credentials"""
    title: str
    """Title of the saved credentials"""

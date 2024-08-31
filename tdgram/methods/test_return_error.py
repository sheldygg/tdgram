from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Error
from .base import BaseMethod


@dataclass(kw_only=True)
class TestReturnError(BaseMethod):
    """
    Returns the specified error and ensures that the Error object is used; for testing only. Can be called synchronously
    """

    __type__: Literal["testReturnError"] = "testReturnError"
    __returning_type__ = Error

    error: Error
    """The error to be returned"""

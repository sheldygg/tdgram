from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CallProblem, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SendCallRating(BaseMethod):
    """
    Sends a call rating
    """

    __type__: Literal["sendCallRating"] = "sendCallRating"
    __returning_type__ = Ok

    call_id: int
    """Call identifier"""
    rating: int
    """Call rating; 1-5"""
    comment: str
    """An optional user comment if the rating is less than 5"""
    problems: list[CallProblem]
    """List of the exact types of problems with the call, specified by the user"""

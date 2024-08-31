from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteBusinessChatLink(BaseMethod):
    """
    Deletes a business chat link of the current account
    """

    __type__: Literal["deleteBusinessChatLink"] = "deleteBusinessChatLink"
    __returning_type__ = Ok

    link: str
    """The link to delete"""

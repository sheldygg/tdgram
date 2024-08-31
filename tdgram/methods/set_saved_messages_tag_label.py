from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, ReactionType
from .base import BaseMethod


@dataclass(kw_only=True)
class SetSavedMessagesTagLabel(BaseMethod):
    """
    Changes label of a Saved Messages tag; for Telegram Premium users only
    """

    __type__: Literal["setSavedMessagesTagLabel"] = "setSavedMessagesTagLabel"
    __returning_type__ = Ok

    tag: ReactionType
    """The tag which label will be changed"""
    label: str
    """New label for the tag; 0-12 characters"""

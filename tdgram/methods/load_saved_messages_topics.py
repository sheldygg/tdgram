from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadSavedMessagesTopics(BaseMethod):
    """
    Loads more Saved Messages topics. The loaded topics will be sent through updateSavedMessagesTopic. Topics are sorted by their topic.order in descending order. Returns a 404 error if all topics have been loaded
    """

    __type__: Literal["loadSavedMessagesTopics"] = "loadSavedMessagesTopics"
    __returning_type__ = Ok

    limit: int
    """The maximum number of topics to be loaded. For optimal performance, the number of loaded topics is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached"""

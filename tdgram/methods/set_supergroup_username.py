from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetSupergroupUsername(BaseMethod):
    """
    Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel
    """

    __type__: Literal["setSupergroupUsername"] = "setSupergroupUsername"
    __returning_type__ = Ok

    supergroup_id: int
    """Identifier of the supergroup or channel"""
    username: str
    """New value of the username. Use an empty string to remove the username. The username can't be completely removed if there is another active or disabled username"""

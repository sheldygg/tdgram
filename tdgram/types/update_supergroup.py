from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Supergroup


@dataclass(kw_only=True)
class UpdateSupergroup(BaseType):
    """
    Some data of a supergroup or a channel has changed. This update is guaranteed to come before the supergroup identifier is returned to the application
    """

    __type__: Literal["updateSupergroup"] = "updateSupergroup"

    supergroup: Supergroup
    """New data about the supergroup"""

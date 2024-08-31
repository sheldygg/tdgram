from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import OptionValue
from .base import BaseMethod


@dataclass(kw_only=True)
class GetOption(BaseMethod):
    """
    Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization. Can be called synchronously for options 'version' and 'commit_hash'
    """

    __type__: Literal["getOption"] = "getOption"
    __returning_type__ = OptionValue

    name: str
    """The name of the option"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class InternalLinkTypeMessageDraft(BaseType):
    """
    The link contains a message draft text. A share screen needs to be shown to the user, then the chosen chat must be opened and the text is added to the input field
    """

    __type__: Literal["internalLinkTypeMessageDraft"] = "internalLinkTypeMessageDraft"

    text: FormattedText
    """Message draft text"""
    contains_link: bool
    """True, if the first line of the text contains a link. If true, the input field needs to be focused and the text after the link must be selected"""

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class ContentBody:
    """
    Represents the body of a content(blog|page|comment|attachment) in confluence.

    This has several different representations which may be present or not.
    """

    def __init__(self, json):  # type: (Dict[str, Any]) -> None
        if 'storage' in json:
            self.storage = json['storage']['value']  # type: str
            self.storage_representation = json['storage']['representation']  # type: str
        if 'editor' in json:
            self.editor = json['storage']['value']  # type: str
            self.editor_representation = json['storage']['representation']  # type: str
        if 'view' in json:
            self.view = json['storage']['value']  # type: str
            self.view_representation = json['storage']['representation']  # type: str
        if 'export_view' in json:
            self.export_view = json['storage']['value']  # type: str
            self.export_view_representation = json['storage']['representation']  # type: str
        if 'styled_view' in json:
            self.styled_view = json['storage']['value']  # type: str
            self.styled_view_representation = json['storage']['representation']  # type: str
        if 'anonymous_export_view' in json:
            self.anonymous_export_view = json['storage']['value']  # type: str
            self.anonymous_export_view_representation = json['storage']['representation']  # type: str

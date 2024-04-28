from typing import Any, Optional

class DefaultDict(dict):
    """A dict that returns a default value if a key is missing."""

    def __init__(self, default: Optional[Any] = None):
        super().__init__()
        self.default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        self[key] = self.default
        return self.default

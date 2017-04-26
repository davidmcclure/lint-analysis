

import attr
import os
import ujson

from core.utils import scan_paths


@attr.s
class Dataset:

    path = attr.ib()

    @classmethod
    def from_local(cls, name):
        """Wrap the local dataset.

        Args:
            name (str): a.json, had.json, etc.

        Returns: cls
        """
        return cls(os.path.join(os.path.dirname(__file__), name))

    def paths(self):
        """Generate segment paths.
        """
        yield from scan_paths(self.path, '\.json$')

    def texts(self):
        """Generate offset sequence rows.
        """
        for path in self.paths():
            with open(path) as fh:
                yield from [ujson.loads(line) for line in fh]

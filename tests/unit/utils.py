"""
PC-BASIC tests.utils
Shared testing utilities

(c) 2020 Rob Hagemans
This file is released under the GNU GPL version 3 or later.
"""

import unittest
import os
import shutil
from unittest import main as run_tests


class TestCase(unittest.TestCase):
    """Base class for test cases."""

    tag = None

    def __init__(self, *args, **kwargs):
        """Define output dir name."""
        unittest.TestCase.__init__(self, *args, **kwargs)
        here = os.path.dirname(os.path.abspath(__file__))
        self._dir = os.path.join(here, u'output', self.tag)
        # does not need to exist
        self._model_dir = os.path.join(here, u'model', self.tag)

    def setUp(self):
        """Ensure output directory exists and is empty."""
        try:
            shutil.rmtree(self._dir)
        except EnvironmentError:
            pass
        os.mkdir(self._dir)

    def output_path(self, *names):
        """Output file name."""
        return os.path.join(self._dir, *names)

    def model_path(self, *names):
        """Model file name."""
        return os.path.join(self._model_dir, *names)

    def get_text_stripped(self, s):
        """Get screen text stripped of trailing spaces."""
        return [_row.rstrip() for _row in s.get_text()]

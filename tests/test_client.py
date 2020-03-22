"""Client application unit testing"""

import os
import sys

if isinstance(sys.path, list) and os.path.dirname(sys.path[0]) not in sys.path:
    sys.path.insert(1, os.path.dirname(sys.path[0]))

from meg_runtime import Config, Plugin, PluginManager

def test_client():
    """TODO: Test client"""
    pass

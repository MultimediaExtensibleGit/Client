"""Multimedia Extensible Git (MEG) Client Application

Git client for multimedia tasks and activities
"""

import sys

# Import MEG runtime
from meg_runtime import App, Config, PluginManager
from meg_runtime.logger import Logger

def main():
    App().run()

# Run MEG client application when executed directly
if __name__ == '__main__':
    main()


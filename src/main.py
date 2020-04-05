"""Multimedia Extensible Git (MEG) Client Application

Git client for multimedia tasks and activities
"""

import sys

# Import MEG runtime
from meg_runtime import Config, PluginManager, UIManager, Logger


# MEG client application
class MEGApp(object):
    """Multimedia Extensible Git (MEG) Client Application"""

    # Constructor
    def __init__(self):
        """Application constructor"""
        # Initialize super class constructor
        super().__init__()
        # Log debug information about home directory
        Logger.debug('MEG: Home <' + Config.get('path/home') + '>')
        # Load configuration
        Config.load()
        # Log debug information about cache and plugin directories
        Logger.debug('MEG: Cache <' + Config.get('path/cache') + '>')
        Logger.debug('MEG: Plugins <' + Config.get('path/plugins') + '>')
        # Update plugins information
        PluginManager.update()
        # Load enabled plugins
        PluginManager.load_enabled()

    # On application started
    def on_start(self):
        """On application started"""
        pass

    # On application stopped
    def on_stop(self):
        """On application stopped"""
        PluginManager.unload_all()

    # Run the application
    def run(self):
        """Build the application UI"""
        # Run the UI
        UIManager.run()


# Run MEG client application when executed directly
if __name__ == '__main__':
    MEGApp().run()

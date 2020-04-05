"""Multimedia Extensible Git (MEG) Client Application

Git client for multimedia tasks and activities
"""

# SDL2 image processing seems to fail so use PIL
import os
if 'KIVY_IMAGE' not in os.environ:
    os.environ['KIVY_IMAGE'] = 'pil'
# Disable Kivy configuration files
if 'KIVY_NO_CONFIG' not in os.environ:
    os.environ['KIVY_NO_CONFIG'] = '1'
# Disable Kivy log files
if 'KIVY_NO_FILELOG' not in os.environ:
    os.environ['KIVY_NO_FILELOG'] = '1'

# Import Kivy and set the minimum required version
import kivy
kivy.require('1.11.0')

# Import Kivy app
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.label import Label

# Import MEG runtime
from meg_runtime import Config, PluginManager, UIManager


# MEG client application
class MEGApp(App):
    """Multimedia Extensible Git (MEG) Client Application"""

    # Constructor
    def __init__(self):
        """Application constructor"""
        # Initialize super class constructor
        super().__init__()
        # Do not allow user to change Kivy settings
        self.use_kivy_settings = False
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

    # Build the application UI
    def build(self):
        """Build the application UI"""
        # Set the application title
        self.title = 'Multimedia Extensible Git'
        # Build the UI
        return UIManager.get_instance()


# Run MEG client application when executed directly
if __name__ == '__main__':
    MEGApp().run()

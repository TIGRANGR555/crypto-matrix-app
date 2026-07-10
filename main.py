"""
CryptoMatrix Application Entry Point
Main Kivy application launcher
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from screens.home_screen import HomeScreen
from screens.settings_screen import SettingsScreen


class CryptoMatrixApp(App):
    """Main application class for CryptoMatrix"""

    def build(self):
        """Build and return the app widget tree"""
        self.title = "CryptoMatrix"
        
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(SettingsScreen(name="settings"))
        
        return sm


if __name__ == "__main__":
    app = CryptoMatrixApp()
    app.run()

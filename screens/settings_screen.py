"""
Settings screen for CryptoMatrix
User preferences and configuration
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class SettingsScreen(Screen):
    """Settings screen for app configuration"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Header
        title = Label(
            text="Settings",
            size_hint_y=0.15,
            font_size="28sp",
            bold=True
        )
        main_layout.add_widget(title)
        
        # Settings content (placeholder)
        settings_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.7)
        settings_layout.add_widget(Label(text="Settings options will appear here"))
        main_layout.add_widget(settings_layout)
        
        # Back button
        button_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.15)
        btn_back = Button(text="Back to Home", background_color=(0.2, 0.8, 0.2, 1))
        btn_back.bind(on_press=self.go_to_home)
        button_layout.add_widget(btn_back)
        main_layout.add_widget(button_layout)
        
        self.add_widget(main_layout)
    
    def go_to_home(self, instance):
        """Navigate back to home screen"""
        self.manager.current = "home"

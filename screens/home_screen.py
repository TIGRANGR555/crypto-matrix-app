"""
Home screen for CryptoMatrix
Primary user interface
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class HomeScreen(Screen):
    """Home screen displaying main app content"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Header
        title = Label(
            text="CryptoMatrix",
            size_hint_y=0.15,
            font_size="32sp",
            bold=True
        )
        main_layout.add_widget(title)
        
        # Content area (placeholder)
        content_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.7)
        content_layout.add_widget(Label(text="Welcome to CryptoMatrix\n\nSelect an option below"))
        main_layout.add_widget(content_layout)
        
        # Button area
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.15)
        
        btn_action = Button(text="Action", background_color=(0.2, 0.6, 0.8, 1))
        btn_settings = Button(text="Settings", background_color=(0.8, 0.6, 0.2, 1))
        btn_settings.bind(on_press=self.go_to_settings)
        
        button_layout.add_widget(btn_action)
        button_layout.add_widget(btn_settings)
        
        main_layout.add_widget(button_layout)
        
        self.add_widget(main_layout)
    
    def go_to_settings(self, instance):
        """Navigate to settings screen"""
        self.manager.current = "settings"

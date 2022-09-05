"""
Basic Kivy GUI built using the Kivy website tutorial.
"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
kivy.require("2.1.0")


class LoginScreen(GridLayout):
    """
    Login screen class used as root widget
    """

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):
    """
    My App
    """
    
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    MyApp().run()

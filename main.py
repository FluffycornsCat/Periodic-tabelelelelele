from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.core.window import Window
class TheScreenManager(ScreenManager):
    pass
class MainScreen(Screen):
    def Exit(self):
        quit()
class default(App):
    def build(self):
        Window.clearcolor = 1,1,1,1
        return TheScreenManager()
default().run()
ok

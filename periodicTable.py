from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.core.window import Window
from PIL import Image
class TheScreenManager(ScreenManager):
    pass
class MainScreen(Screen):

    def Exit(self):
        quit()
class default1(App):
    def build(self):
        Window.clearcolor = 1,1,1,1
        return TheScreenManager()

default1().run()

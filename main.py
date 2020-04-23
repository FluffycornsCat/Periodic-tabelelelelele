from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
import database

class TheScreenManager(ScreenManager):
    pass

class MainScreen(Screen):

    def okk(self):
        global textGrundstoffer
        try:
            command = "database." + self.ids["SearchBar"].text
            textGrundstoffer = eval(command)
        except AttributeError:
            textGrundstoffer = "No results found for '" + self.ids["SearchBar"].text + "'"

        self.PopUp()


    def PopUp(self):
        PopupLayout = BoxLayout(orientation= "vertical")
        #image=Image(source= 'files/loading.gif', anim_delay= 0)
        label=Label(text=textGrundstoffer)
        #content.add_widget(image)
        PopupLayout.add_widget(label)
        #button1 = Button(text="Close", size_hint=(1, .5))
        #button1.bind(on_press=popup.dismiss)
        #WrongPassword.add_widget(button1)
        popup = Popup(title= self.ids["SearchBar"].text,
                  size_hint=(.5, .5),
                  content=WrongPassword, auto_dismiss=True)

        popup.open()

class default(App):
    def build(self):




        Window.clearcolor = 1,1,1,1
        return TheScreenManager()
default().run()

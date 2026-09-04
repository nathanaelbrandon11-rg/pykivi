import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="This is the first screen"))
        self.add_widget(Button(text="Go to Second Screen", on_press=self.go_to_second))

    def go_to_second(self, instance):
        self.parent.current = "second"
        

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="This is the second screen"))
        self.add_widget(Button(text="Go Back", on_press=self.go_back))

    def go_back(self, instance):
        self.parent.current = "first"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm
app = MyApp()
app.run()
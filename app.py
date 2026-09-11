#------------IMPORTS----------------#
from asyncio import Runner

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from instructions import *
from ruffier import *
from seconds import Seconds


#------------VARIABLES--------------#

name = "" 
age =  0
Window.clearcolor = (0.32, 0.54, 0.54, 0.19)
btn_color = (0.98, 0.23, 0.8, 19)

#------------SCREENS----------------#


def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False



class InstructionScreen(Screen):
    def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       instr = Label(text=txt_instruction)
 
       lbl1 = Label(text='Enter your name:', halign='right')
       self.in_name = TextInput(multiline=False)
       lbl2 = Label(text='Enter your age:', halign='right')
 
       self.in_age = TextInput(text='7', multiline=False)
       self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
       line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
       line1.add_widget(lbl1)
       line1.add_widget(self.in_name)
       line2.add_widget(lbl2)
       line2.add_widget(self.in_age)
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line1)
       outer.add_widget(line2)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)



    def next(self):
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age == False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'


class PulseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        self.next_screen = False
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Enter the result:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line1.add_widget(lbl_result)
        line1.add_widget(self.in_result)

        self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Next'


    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 < 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'
                


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = Label(text=txt_sits,size_hint=(0.5, 1))
        self.lbl_sits = Sits(30)
        self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        line = BoxLayout()
        vlay = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        vlay.add_widget(self.lbl_sits)
        line.add_widget(vlay)
        line.add_widget(self.run)

        self.btn = Button(text= 'Start Squats', size_hint=(0.3, 0.2),pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next_screen

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)




class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstructionScreen(name='instruction'))
        sm.add_widget(PulseScreen(name='pulse1'))
        return sm




app = MainApp()
app.run()

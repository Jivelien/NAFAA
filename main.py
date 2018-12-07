from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color #TMP
from kivy.graphics.vertex_instructions import Rectangle #TMP
from kivy.properties import NumericProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from random import random

class Parameters(FloatLayout):
    pass

class TrainingLayout(BoxLayout):
    counter=NumericProperty(0)
    isParameter=BooleanProperty(False)
    isPause=BooleanProperty(True)
    isRunning=BooleanProperty(False)
    pictureList=ListProperty({'A','B','C','D','E','F','G'})
    currentPictureId=NumericProperty(0)

    def start_stretching(self, *args):
        self.isPause = not self.isPause
        if not self.isRunning:
            self.clock_event = Clock.schedule_interval(self.picture_time, 1)
            self.isRunning=True

    def picture_time(self, *args):
        stretchImage = self.ids.stretchImage
        stretchImage.source = './img/'+self.pictureList[self.currentPictureId]+'.jpg'
        print(self.currentPictureId)
        #print(self.counter)
        if self.counter==2 and self.currentPictureId==6:
            stretchImage.source = ''
            self.clock_event.cancel()
            self.counter=0
            self.isPause= True
            self.isRunning=False
        elif self.counter==2:
            self.currentPictureId+=1
            self.counter=0
        if not self.isPause:
            self.counter+=1

    def show_parameters(self, *args):
        if self.isParameter == False :
            self.parent.add_widget(Parameters())
            self.isParameter = True
        else:
            self.parent.remove_widget(self.parent.children[0])
            self.isParameter = False

    

class TopBar(BoxLayout):
    pass

class PictureBox(BoxLayout):
    pass
class SeriesBox(BoxLayout):
    pass
class ActionBox(BoxLayout):
    pass
class Parameters(BoxLayout):
    pass

class TrainingApp(App):
    def build(self):
        return TrainingLayout()

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size=(428,762)

    TrainingApp().run()
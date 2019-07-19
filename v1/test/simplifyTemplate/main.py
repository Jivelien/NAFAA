from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color #TMP
from kivy.graphics.vertex_instructions import Rectangle #TMP
from kivy.properties import NumericProperty 
from kivy.clock import Clock

class TrainingLayout(BoxLayout):
    counter=NumericProperty(0)

    def picture_time(self, *args):
        stretchImage = self.ids.stretchImage
        self.counter+=1
        if self.counter==5:
            stretchImage.source = ''
            self.clock_event.cancel()
            self.counter=0

    def start_stretching(self, *args):
        stretchImage = self.ids.stretchImage
        stretchImage.source = './img/A.jpg'
        try:
            self.clock_event.cancel()
            self.counter=0
        except:
            pass
        self.clock_event = Clock.schedule_interval(self.picture_time, 1)
    
    def show_menu(self, *args):
        popup = Popup(title='Test popup',
        content=Label(text='Hello world'),
        size_hint=(None, None), size=(400, 400))
        popup.open()

class TopBar(BoxLayout):
    def show_menu(self, *args):
        popup = Popup(content=Parameters(),
                            title_size='0sp',
                            size_hint=(None, None),
                            size=(400, 400))

        popup.open()

class PictureBox(BoxLayout):
    pass
class SeriesBox(BoxLayout):
    pass
class Parameters(BoxLayout):
    pass

class TrainingApp(App):
    def build(self):
        return TrainingLayout()

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size=(571,1016)

    TrainingApp().run()
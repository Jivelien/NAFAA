from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color #TMP
from kivy.graphics.vertex_instructions import Rectangle #TMP

class TrainingLayout(BoxLayout):
    pass


class TrainingApp(App):
    def build(self):
        return TrainingLayout()

if __name__ == '__main__':
    Window.clearcolor = (1, 1, 1, 1)
    Window.size=(571,1016)

    TrainingApp().run()
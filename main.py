from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MainWidget(Widget):
    def checkbox_click(self, instance, value):
        pass


class BSCSapp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)


BSCSapp().run()


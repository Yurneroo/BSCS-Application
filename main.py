from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


class MainWidget(Widget):
    def checkbox_click(self, instance, value):
        pass


class BSCS_login_page(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)


class BSCS_main_page(App):
    pass


BSCS_login_page().run()
BSCS_main_page().run()

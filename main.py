from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (480, 800)


class MainWidget(FloatLayout):

    screen_manager = ObjectProperty(None)


class BSCSApp(MDApp):
    def build(self):
        return Builder.load_file("widget.kv")


if __name__ == "__main__":
    BSCSApp().run()

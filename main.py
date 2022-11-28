import kivy
from kivy.properties import ListProperty
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import mysql.connector

Window.size = (480, 800)


class BSCSLoginPage(MDApp):
    pass


class BSCSMainPage(MDApp):
    pass


class BSCSApp(MDApp):
    def build(self):
        return Builder.load_file("BSCSMainPage.kv")


if __name__ == "__main__":
    BSCSMainPage().run()

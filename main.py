import kivy
from kivy.properties import ListProperty
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import mysql.connector

Window.size = (480, 800)


class BSCSLoginPage(MDApp):

    database = mysql.connector.Connect(host="localhost", user="root", password="2004130304", database="loginform")
    cursor = database.cursor()
    cursor.execute("select * from logindata")
    for i in cursor.fetchall():
        print(i[0], i[1]) 

def send_data(self, email, password):
#here is the function to send data from python to mysql
        self.cursor.execute(f"insert into logindata values('{email.text}', '{password.text}')")
        self.database.commit()
        for i in self.cursor.fetchall():
            print(i[0], i[1])



class BSCSMainPage(MDApp):
    def build(self):
        return


BSCSLoginPage().run()

from tokenize import Name
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.core.window import Window
Window.size = (500, 500)

KV = '''
MDBoxLayout:
    pos_hint: {'center_x': .5, 'center_y': .5}
    spacing: "25dp"
    size_hint: None, None
    size: "500dp", "500dp"
    orientation: "vertical"
    padding: 25

    MDTextField:
        id: textBox_Login
        hint_text: "Login"
        mode: "round"
        max_text_length: 15
        helper_text: "Massage"

    MDTextField:
        id: textBox_Password
        hint_text: "Password"
        mode: "round"
        max_text_length: 15
        helper_text: "Massage"

    MDFillRoundFlatButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        size: "100", "100"
        text: "sign up"
        on_press: app.clickRegButton(textBox_Login, textBox_Password)

    MDFillRoundFlatButton:
        pos_hint: {'center_x': .5, 'center_y': .5}
        size: "100", "100"
        text: "sign in"
        on_press: app.clickSignUpButton(textBox_Login, textBox_Password)

    MDFloatingActionButtonSpeedDial:
        data: app.data
        root_button_anim: True
        hint_animation: True
        bg_hint_color: app.theme_cls.primary_light
'''

class Example(MDApp):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
        'C#': 'language-cs',
    }

    def build(self):
        return Builder.load_string(KV)

    def clickRegButton(self, textBoxlogin, textBoxPass):
        file = open("UserData.txt", 'w')
        file.write("Login:" + textBoxlogin.text + "\n")
        file.write("Password:" + textBoxPass.text + "\n")
        file.close()

    def clickSignUpButton(self, textBoxlogin, textBoxPass):
        if len(textBoxlogin.text) == 0 and len(textBoxPass.text) == 0:
            return
            
        file = open("UserData.txt", 'r')
        UsersData = [line.strip().replace("Login:","").replace("Password:","") for line in file]

        for i in range(len(UsersData)):
            if (i % 2 != 0) : continue

            if UsersData[i] == textBoxlogin.text and UsersData[i + 1] == textBoxPass.text:
                print("Good")

        file.close()


Example().run()


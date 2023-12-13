from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        but = Button(text='Hello', size_hint=(.5, .2),pos_hint={'x': .25, 'y': .4})
        return but


if __name__ == '__main__':
    TestApp().run()

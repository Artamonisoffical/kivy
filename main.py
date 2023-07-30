from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.layout import Widget
from kivy.uix.label import Label
from kivy.graphics import Rotate
from kivy.clock import Clock
from random import randint as rnd


from kivy.config import Config
Config.set("graphics", "resizable", '0')
Config.set("graphics", "width", 900)
Config.set("graphics", "height", 500)

class Game(Widget):
    def __init__(self,**kwargs):
        super(Game, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if len(app.lines) > 0:
            if app.lines[0].pos[1] > 180 and app.lines[0].pos[1] < 220:
                with app.game.canvas:
                    Color(.45, .95, 1, 1)
                    Rectangle(pos=app.lines[0].pos, size=(300, 20))
                    Color(0, 0, 0, .5)
                    Rectangle(pos=app.lines[0].pos, size=(300, 20))
                    app.score.text = str(int(app.score.text) + 1)
                del app.lines[0]
                if int(app.score.text) % 5 == 0:
                    app.speed += 2
                    if app.rate > 2: app.rate -= 2
            else:
                app.reset()

class Application(App):
    def reset(self):
        with self.game.canvas:
            for i in range(len(app.lines)):
                Color(.45, .95, 1, 1)
                Rectangle(pos=app.lines[i].pos, size=(300, 20))
                Color(0, 0, 0, .5)
                Rectangle(pos=app.lines[i].pos, size=(300, 20))

        self.score.text = "0"
        self.rate = 50
        self.speed = 10
        self.lines = []

    def loop(self, dt):
        if self.isGame:
            with self.game.canvas:
                if rnd(0, self.rate) == 0:
                    if len(self.lines) == 0 or self.lines[len(self.lines)-1].pos[1] < Window.size[1]-25:
                        Color(1, 0, 0, 1)
                        self.lines.append(Rectangle(pos=(Window.size[0]/2-150, Window.size[1]), size=(300, 20)))
                Color(1, 1, 1, 1)
                Rectangle(pos=(Window.size[0]/2-150, 200), size=(300, 20))
                for i in range(len(self.lines)):
                    self.lines[i].pos = (Window.size[0]/2-150, self.lines[i].pos[1]-self.speed)
                    if self.lines[i].pos[1] <= 20:
                        self.reset()
                        break
                        
        else:
            if self.text.font_size != 90:
                self.text.font_size += self.num[0]

    def click(self, inst):
        inst.disabled = True
        self.isGame = True
        with self.game.canvas:
            Color(.45, .95, 1, 1)
            Rectangle(pos=(0, 0), size=Window.size)
            Color(0, 0, 0, .5)
            Rectangle(pos=(Window.size[0]/3, 0), size=(Window.size[0]/3, Window.size[1]))
        self.score = Label(text="0", font_size=50, pos=(0, 0), color="black")
        self.game.add_widget(Game())
        self.game.add_widget(self.score)

    def build(self):
        Clock.schedule_interval(self.loop, 1 / 50)

        self.color = [0, 0, 0, 1]
        self.timer = 2
        self.num = [1, 1]
        self.rate = 50
        self.speed = 10
        self.lines = []
        self.isGame = False

        self.game = Widget()
        self.text = Label(text="Reaction game", font_size=30, color=self.color)
        self.text.pos = (Window.size[0]/2-self.text.size[0]/2, Window.size[1]/2-50-self.text.size[1]/2+300)
        self.button = Button(text="PLAY", font_size=30, size=[200, 100], background_color=self.color, on_press=self.click, pos=(Window.size[0]/2-100, Window.size[1]/2-50))
        
        with self.game.canvas:
            Color(1, 1, 1, 1)
            Rectangle(position=(0, 0), size=Window.size)
            
        self.game.add_widget( self.text )
        self.game.add_widget( self.button )

        return self.game

if __name__ == "__main__":
    app = Application()
    app.run() 

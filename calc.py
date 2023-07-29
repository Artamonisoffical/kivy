from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


from kivy.config import Config
Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)


class Application(App):

    def ans(self, instance):
        self.text.text = str(eval(self.text.text))

    def num(self, instance):
        if self.text.text == "0" and instance.text != ".": self.text.text = ""
        self.text.text += instance.text.replace("X", "*").replace("x²", "**2")

    def cls(self, instance):
        self.text.text = "0"

    def nah(self, instance):
        self.text.text = self.text.text[:-1]

    def build(self):
        self.text = Label( text="0", font_size=20 )
        
        grid = GridLayout(cols=4, spacing=2)
        box = BoxLayout(orientation="vertical", padding=[25])

        box.add_widget( self.text )
        
        grid.add_widget( Button(text="C", font_size=30, on_press=self.cls) )
        grid.add_widget( Button(text="<", font_size=30, on_press=self.nah) )
        grid.add_widget( Button(text="x²", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="/", font_size=30, on_press=self.num) )

        grid.add_widget( Button(text="7", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="8", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="9", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text=" X ", font_size=30, on_press=self.num) ) 

        grid.add_widget( Button(text="4", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="5", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="6", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text=" - ", font_size=30, on_press=self.num) )
        
        grid.add_widget( Button(text="1", font_size=30, on_press=self.num))
        grid.add_widget( Button(text="2", font_size=30, on_press=self.num))
        grid.add_widget( Button(text="3", font_size=30, on_press=self.num))
        grid.add_widget( Button(text=" + ", font_size=30, on_press=self.num))
        
        grid.add_widget( Widget() )
        grid.add_widget( Button(text="0", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text=".", font_size=30, on_press=self.num) )
        grid.add_widget( Button(text="=", font_size=30, on_press=self.ans) )

        box.add_widget(grid)

        return box


if __name__ == "__main__":
    Application().run() 
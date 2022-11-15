import pyglet
import os

class Louncher_window(pyglet.window.Window):
    def __init__(self, **args,):
        super().__init__(**args)
    
    def on_draw(self):
        self.clear()
        walpapper = pyglet.sprite.Sprite(img = pyglet.image.load('walpapper.png'))
        walpapper.draw()



class Louncher:
    def __init__(self) -> None:
        self.window = Louncher_window(width = 800, height = 600, caption = 'Louncher for <My minecraft>', resizable = False, vsync = False)
        
    def run(self):
        pyglet.app.run()


if __name__ == '__main__':
    louncher = Louncher()
    louncher.run()
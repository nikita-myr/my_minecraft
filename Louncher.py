import pyglet
import os

WALPAPPER = pyglet.sprite.Sprite(img = pyglet.image.load('walpapper.png'))
PLAY_BUTTON = pyglet.sprite.Sprite(img= pyglet.image.load('play_button.png'), x=300, y=350)
QUIT_BUTTON= pyglet.sprite.Sprite(img= pyglet.image.load('quit_button.png'), x=300, y=170)

class Louncher_window(pyglet.window.Window):
    def __init__(self, **args,):
        super().__init__(**args)
    
    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            if x <= 500 and x >= 300 and y >= 350 and y <= 412:
                path = os.getcwd
                os.system(f'cd {path}')
                os.system('python3 main.py')
                louncher.quit()
            elif x<= 500 and x >= 300 and y >= 170 and y <= 232:
                louncher.quit()
                
    def on_draw(self):
        self.clear()
        WALPAPPER.draw()
        PLAY_BUTTON.draw()
        QUIT_BUTTON.draw()


class Louncher:
    def __init__(self) -> None:
        self.window = Louncher_window(width = 800, height = 600, caption = 'Louncher for <My minecraft>',
                                      resizable = False, vsync = False
                                      )
        
    def run(self):
        pyglet.app.run()

    def quit(self):
        self.window.close()
    

if __name__ == '__main__':
    louncher = Louncher()
    louncher.run()
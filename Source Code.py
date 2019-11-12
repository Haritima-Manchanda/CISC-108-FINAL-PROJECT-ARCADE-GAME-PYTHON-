import arcade
SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000
SCREEN_TITLE="X COSMOS"

class X_COSMOS(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

    def on_draw(self):
        arcade.start_render()

def main():
    window=X_COSMOS()
    window.setup()
    arcade.run()

if __name__=="__main__":
    main()

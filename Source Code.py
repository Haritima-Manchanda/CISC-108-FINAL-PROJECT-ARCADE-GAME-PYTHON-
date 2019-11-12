import arcade
SCREEN_WIDTH=1000
SCREEN_HEIGHT=800
SCREEN_TITLE="X COSMOS"
CHARACTER_SCALING=0.25

class X_COSMOS(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.score=0
        self.player_list=None
        self.background_list=None

    def setup(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)
        self.player_list=arcade.SpriteList()
        self.player_sprite=arcade.Sprite("images/Character1.png",CHARACTER_SCALING)
        self.player_sprite.center_x=500
        self.player_sprite.center_y = 500
        self.player_list.append(self.player_sprite)
        self.background_list=arcade.SpriteList()
        self.background=arcade.Sprite("images/background1.png")
        self.background.center_x=500
        self.background.center_y=500
        self.background_list.append(self.background)


    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.background_list.draw()
        arcade.draw_text(str("SCORE:"), 0, 0, arcade.color.BLACK, 50)
        arcade.draw_text(str("LEVEL:"), 350, 0, arcade.color.BLACK, 50)
def main():
    window=X_COSMOS()
    window.setup()
    arcade.run()

if __name__=="__main__":
    main()


import arcade
import random

""" 
    RESOURCES
    arcade.academy
    wikipedia

"""

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "X COSMOS"
CHARACTER_SCALING = 0.25

allowed_jumps = 5
spike_distance = 20
LEFT_VIEWPORT_MARGIN = 150
RIGHT_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100
VIEWPORT_MARGIN=40

class X_COSMOS(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.time = 0
        self.score = 0
        self.level = 0
        self.lives = 0
        self.player_list = None
        self.background_list=self.background= None
        self.spike_list = None
        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/character2.png", 1.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        self.background=arcade.load_texture("images/background1.png")
        self.spike_list = arcade.SpriteList()
        for i in range(1, 3):
            self.spike_sprite = arcade.Sprite("images/spikes.png", 0.8)
            self.spike_sprite.center_x = 200 + 5 * i * spike_distance
            self.spike_sprite.center_y = 270
            self.spike_list.append(self.spike_sprite)
        self.coin_list=arcade.SpriteList()
        for i in range(5):
            self.coin_sprite = arcade.Sprite("images/Coin.png", 0.8)
            self.coin_sprite.center_x = random.randrange(400,1000,50)
            self.coin_sprite.center_y = 270
            self.coin_list.append(self.coin_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.spike_list)

        self.view_left = 0
        self.view_bottom = 0
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
        self.background = arcade.load_texture("images/background1.png")

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(500+self.view_left,400+self.view_bottom,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


        self.player_list.draw()
        self.spike_list.draw()
        self.coin_list.draw()

        arcade.draw_text(str("SCORE:"), 30+self.view_left, 90+self.view_bottom, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.score), 200+self.view_left, 90+self.view_bottom, arcade.color.RED, 40)
        arcade.draw_text(str("LEVEL:"), 370+self.view_left, 90+self.view_bottom, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.level), 530+self.view_left, 90+self.view_bottom, arcade.color.RED, 40)
        arcade.draw_text(str("LIVES:"), 720+self.view_left, 90+self.view_bottom, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.lives), 850+self.view_left, 90+self.view_bottom, arcade.color.RED, 40)
        arcade.draw_text(str("TIMER IN SEC: "), 610+self.view_left, 700+self.view_bottom, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.time), 900+self.view_left, 700+self.view_bottom, arcade.color.RED, 40)


    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = 30
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -30
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 30

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()
        self.time += (round(delta_time)%0.1)

        changed = False
        # Scroll right
        right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

def main():
    window = X_COSMOS()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()











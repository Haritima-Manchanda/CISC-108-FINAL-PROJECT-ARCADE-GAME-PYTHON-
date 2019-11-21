"""
import arcade
SCREEN_WIDTH=1000
SCREEN_HEIGHT=800
SCREEN_TITLE="X COSMOS"
allowed_jumps=5
spike_distance=20

class USER_INPUT(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.name=None
        self.age=None
        self.question="So, ARE YOU READY??"
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

    def input(self):
        self.name=input("Enter your name")
        self.age=int(input("Enter your age: "))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str("WHAT IS YOUR NAME:"), 200, 500, arcade.color.RED, 40)
        arcade.draw_text(str(self.name),800,500,arcade.color.RED)
        arcade.draw_text(str("WHAT IS YOUR AGE:"), 200, 300, arcade.color.RED, 40)


class player(arcade.Sprite):
    def __init__(self):
        super().__init__("images/character2.png",1)
        self.center_x = 50
        self.center_y = 250

class background(arcade.Sprite):
    def __init__(self):
        super().__init__("images/background1.png",1)
        self.center_x=500
        self.center_y=500

class spikes(arcade.Sprite):
    def __init__(self):
        super().__init__("images/spikes.png",0.8)
        for i in range(2):
            self.center_x = 200 + 5 * i * spike_distance
            self.center_y = 240

class lives(arcade.Sprite):
    def __init__(self):
        super().__init__("images/lives.png")
        self.center_x=100
        self.center_y=600
        self.life_speed=50

class XCOSMOS(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.time = 0
        self.score = 0
        self.level = 1
        self.lives = 1
        self.player_list = self.coin_list = self.lives_list=None
        self.background_list =None
        self.spike_list = None
        self.coin_collision_list=self.life_collision_list=self.spike_collision_list=None
        self.physics_engine = None
        self.life_speed=50
        self.view_left=0

    def setup(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

        #self.user_input_list=arcade.SpriteList()
        #self.user_input_list.append(USER_INPUT())


        self.player_list = arcade.SpriteList()
        self.player_list.append(player())

        self.background_list=arcade.SpriteList()
        self.background_list.append(background())

        self.spike_list=arcade.SpriteList()
        self.spike_list.append(spikes())


        self.coin_list=arcade.SpriteList()
        for i in range(0,5):
            self.coin_sprite=arcade.Sprite("images/Coin.png",0.6)
            self.coin_sprite.center_x=50*i+600
            self.coin_sprite.center_y=200
            self.coin_list.append(self.coin_sprite)

        self.lives_list=arcade.SpriteList()
        self.lives_list.append(lives())


        self.physics_engine = arcade.PhysicsEngineSimple(self.player_list[0], self.spike_list)

    def on_draw(self):

        arcade.start_render()
        self.user_input_list.draw()
        self.background_list.draw()
        self.player_list.draw()
        self.spike_list.draw()
        self.coin_list.draw()
        self.lives_list.draw()

        arcade.draw_text(str("SCORE:"), 30, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.score), 200, 90, arcade.color.RED, 40)
        arcade.draw_text(str("LEVEL:"), 370, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.level), 530, 90, arcade.color.RED, 40)
        arcade.draw_text(str("LIVES:"), 720, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.lives), 850, 90, arcade.color.RED, 40)
        arcade.draw_text(str("TIMER IN SEC: "), 600, 700, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.time),890, 700, arcade.color.RED, 40)

    def on_key_press(self, key, modifiers):
        for player in self.player_list:
            if key == arcade.key.UP:
                if player.center_y<=600:
                    player.change_y=30
            elif key==arcade.key.DOWN:
                if player.center_y>=270:
                    player.change_y=-30
            elif key==arcade.key.RIGHT:
                player.change_x=30


    def on_key_release(self, key, modifiers):
        for player in self.player_list:
            if key == arcade.key.UP:
                player.change_y = 0
            elif key == arcade.key.DOWN:
                player.change_y = 0
            elif key == arcade.key.RIGHT:
                player.change_x = 0


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.time += (round(delta_time) + 1) % 0.1

        self.coin_collision_list = arcade.check_for_collision_with_list(self.player_list[0], self.coin_list)
        self.life_collision_list= arcade.check_for_collision_with_list(self.player_list[0], self.lives_list)

        for coin in self.coin_collision_list:
            coin.remove_from_sprite_lists()
            self.score += 10

        for life in self.life_collision_list:
            life.remove_from_sprite_lists()
            self.lives+=1




def main():
    #object=USER_INPUT()
    window = USER_INPUT()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
"""

import arcade
import random
SCREEN_WIDTH=1000
SCREEN_HEIGHT=1000
SCREEN_TITLE="SNAKE GAME"

LEFT_VIEWPORT_MARGIN = 150
RIGHT_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

class SNAKE_GAME(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.snake_list=self.tile_list=self.physics_engine=self.tile_collision_list=self.coin_collision_list=None
        self.score=0
        self.length=0
        self.snake_sprite=None
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.view_bottom = 0
        self.view_left = 0

        self.snake_list = arcade.SpriteList()
        self.snake_sprite = arcade.Sprite("images/character2.png",1)
        self.snake_sprite.center_x =500
        self.snake_sprite.center_y =250
        self.snake_list.append(self.snake_sprite)

        self.tile_list=arcade.SpriteList()
        for i in range(500,1650,210):
            for j in range(0,1000,64):
                if random.randrange(5)>0:
                    self.tile_sprite = arcade.Sprite("images/tile.png", 0.4)
                    self.tile_sprite.center_x=j
                    self.tile_sprite.center_y=i
                    self.tile_list.append(self.tile_sprite)

        self.coin_list = arcade.SpriteList()
        for i in range(5):
            self.coin_sprite = arcade.Sprite("images/Coin.png", 0.6)
            self.coin_sprite.center_x = random.randrange(10,900)
            self.coin_sprite.center_y = random.randrange(400,900)
            self.coin_list.append(self.coin_sprite)


        self.physics_engine = arcade.PhysicsEngineSimple(self.snake_sprite, self.tile_list)

    def on_draw(self):
        arcade.start_render()
        self.snake_list.draw()
        self.tile_list.draw()
        self.coin_list.draw()
        arcade.draw_text(str("SCORE:"),800, 900, arcade.color.RED, 40)
        arcade.draw_text(str(self.score), 950, 900, arcade.color.RED, 40)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.snake_sprite.change_y = 10
        elif key == arcade.key.DOWN:
            if self.snake_sprite.center_y>=300:
                self.snake_sprite.change_y = -10
        elif key == arcade.key.RIGHT:
            if self.snake_sprite.center_x<900:
                self.snake_sprite.change_x =10
        elif key == arcade.key.LEFT:
            if self.snake_sprite.center_x>100:
                self.snake_sprite.change_x =-10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.snake_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.snake_sprite.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake_sprite.change_x = 0
        elif key == arcade.key.LEFT:
            self.snake_sprite.change_x = 0

    def on_update(self, delta_time):
        self.physics_engine.update()

        self.tile_collision_list = arcade.check_for_collision_with_list(self.snake_sprite, self.tile_list)
        self.coin_collision_list = arcade.check_for_collision_with_list(self.snake_sprite, self.coin_list)


        for tile in self.tile_collision_list:
            self.score=-10
        for coin in self.coin_collision_list:
            coin.remove_from_sprite_lists()
            self.score+=1
        changed = False

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.snake_sprite.top > top_boundary:
            self.view_bottom += self.snake_sprite.top - top_boundary
            changed = True
        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left - 1,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom - 1)


def main():
    window = SNAKE_GAME()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()








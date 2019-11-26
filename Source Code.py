import arcade
import random
WINDOW_WIDTH=1000
WINDOW_HEIGHT=1000
GAME_TITLE="X COSMOS"
BULLET_SPEED=5

class X_COSMOS(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH,WINDOW_HEIGHT,GAME_TITLE)
        self.score=0
        self.level=0
        self.bullet_list=self.collision_list=None
        self.player_list=self.bubble_list=self.physics_engine=None

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.player_list=arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/character2.png", 1)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y =250
        self.player_list.append(self.player_sprite)

        self.bubble_list=arcade.SpriteList()
        for i in range(50):
            self.bubble_sprite=arcade.Sprite("images/Coin.png",0.40)
            self.bubble_sprite.center_x=random.randrange(50,950,30)
            self.bubble_sprite.center_y=600
            self.bubble_list.append(self.bubble_sprite)
        self.bullet_list=arcade.SpriteList()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.bubble_list)
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.bubble_list.draw()
        self.bullet_list.draw()
        arcade.draw_text(str("SCORE: "),700, 900, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.score),900, 900, arcade.color.WHITE, 40)

    def on_key_press(self,key,modifiers):
        if key==arcade.key.RIGHT:
            if self.player_sprite.center_x<=935:
                self.player_sprite.change_x=15
        elif key==arcade.key.LEFT:
            if self.player_sprite.center_x>=45:
                self.player_sprite.change_x=-15
        elif key==arcade.key.UP:
            bullet=arcade.Sprite("images/snake2.png",0.3)
            bullet.change_y=BULLET_SPEED
            bullet.center_x=self.player_sprite.center_x
            bullet.bottom=self.player_sprite.top

            self.bullet_list.append(bullet)


    def on_key_release(self,key, modifiers):
        if key==arcade.key.RIGHT:
            self.player_sprite.change_x=0
        elif key==arcade.key.LEFT:
            self.player_sprite.change_x=0

    def on_update(self,delta_time):
        self.physics_engine.update()
        self.bullet_list.update()
        for bullet in self.bullet_list:
            self.collision_list=arcade.check_for_collision_with_list(bullet,self.bubble_list)
            for bubble in self.collision_list:
                bullet.remove_from_sprite_lists()
                bubble.remove_from_sprite_lists()
                self.score+=1
            if bullet.bottom>WINDOW_HEIGHT:
                bullet.remove_from_sprite_lists()
                self.score-=10



def main():
    """ Main method """
    window = X_COSMOS()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

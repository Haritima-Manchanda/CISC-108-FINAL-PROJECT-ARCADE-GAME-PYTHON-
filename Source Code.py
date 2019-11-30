import arcade
import random
WINDOW_WIDTH=1000
WINDOW_HEIGHT=1000
GAME_TITLE="X COSMOS"
BULLET_SPEED=5
BUBBLE_MOVEMENT=2


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("INSTRUCTIONS SCREEN",500,500,arcade.color.WHITE,40)
        arcade.draw_text("CLICK TO PLAY",500,400,arcade.color.WHITE,40)
    def on_mouse_press(self,x,y,button,modifiers):
        game_view=X_COSMOS()
        self.window.show_view(game_view)

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MENU",500,500,arcade.color.WHITE,40)
        arcade.draw_text("CLICK TO PLAY",500,400,arcade.color.WHITE,40)
    def on_mouse_press(self,x,y,button,modifiers):
        instructions_view=InstructionView()
        self.window.show_view(instructions_view)

class LEVEL2(arcade.Sprite):
    def update(self):
        self.center_x+=BUBBLE_MOVEMENT
        if self.center_x>1000:
            self.center_x=0

class LEVEL3(arcade.Sprite):
    def update(self):
        self.center_x += BUBBLE_MOVEMENT
        if self.center_x==1000 and self.center_y>=500:
            self.center_y -=50
            self.center_x=0
        elif self.center_x==0 and self.center_y>=500:
            self.center_y-=50
            self.center_x==0


class X_COSMOS(arcade.View):
    def __init__(self):
        super().__init__()
        self.score=0
        self.level=1
        self.bullet_list=self.collision_list=self.physics_engine=None
        self.player_list=self.bubble_list=None

    def level_1(self):
        self.bubble_list = arcade.SpriteList()
        for i in range(50):
            self.bubble_sprite = arcade.Sprite("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 600
            self.bubble_list.append(self.bubble_sprite)

    def level_2(self):
        for i in range(50):
            self.bubble_sprite=LEVEL2("images/Coin.png",0.40)
            self.bubble_sprite.center_x=random.randrange(50,950,30)
            self.bubble_sprite.center_y=600
            self.bubble_list.append(self.bubble_sprite)

    def level_3(self):
        for i in range(50):
            self.bubble_sprite=LEVEL3("images/Coin.png",0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 750
            self.bubble_list.append(self.bubble_sprite)


    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.player_list=arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/character2.png", 1)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y =250
        self.player_list.append(self.player_sprite)

        self.bullet_list=arcade.SpriteList()
        self.level_1()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.bubble_list)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.bubble_list.draw()
        self.bullet_list.draw()
        arcade.draw_text(str("SCORE: "),700, 900, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.score),900, 900, arcade.color.WHITE, 40)
        arcade.draw_text(str("LEVEL: "), 700, 800, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.level), 900, 800, arcade.color.WHITE, 40)

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
        self.bubble_list.update()
        for bullet in self.bullet_list:
            self.collision_list=arcade.check_for_collision_with_list(bullet,self.bubble_list)
            for bubble in self.collision_list:
                bullet.kill()
                bubble.kill()
                self.score+=1
            if bullet.bottom>WINDOW_HEIGHT:
                bullet.kill()
                self.score-=10
            if len(self.bubble_list)==0 and self.level==1:
                self.level+=1  # Increase the Level
                self.score=0  # Reset the score
                self.level_2()
            elif len(self.bubble_list)==0 and self.level==2:
                self.level+=1  # Increase the Level
                self.score=0  # Reset the score
                self.level_3()


def main():
    """ Main method """
    window=arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT,GAME_TITLE)
    menu_view=MenuView()
    window.show_view(menu_view)
    arcade.run()
    """ 
    window = X_COSMOS()
    window.setup()
    arcade.run()"""


if __name__ == "__main__":
    main()

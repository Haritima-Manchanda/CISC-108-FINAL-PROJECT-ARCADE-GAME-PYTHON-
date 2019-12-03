import arcade
import random
WINDOW_WIDTH=1000
WINDOW_HEIGHT=1000
GAME_TITLE="X COSMOS"
BULLET_SPEED=5
BUBBLE_MOVEMENT=2


class InstructionView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.MAROON)
        self.buttons = arcade.SpriteList()
        self.button_sprite = arcade.Sprite("images/star.png", 2)
        self.button_sprite.center_x = 700
        self.button_sprite.center_y = 300
        self.buttons.append(self.button_sprite)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("INSTRUCTIONS",250,900,arcade.color.WHITE,40)
        arcade.draw_text("Shoot the Bubbles with the help of bullets.",10,800,arcade.color.WHITE,30,italic=True)
        arcade.draw_text("The player could move by pressiong the keyboard keys.",10,700,arcade.color.WHITE,30)
        arcade.draw_text("The bullets will be fired on clicking the upper headed arrow key.",10,600,arcade.color.WHITE,30)
        arcade.draw_text("CLICK STAR TO PLAY",500,400,arcade.color.WHITE,40)
        self.buttons.draw()

    def on_mouse_press(self,x,y,button,modifiers):
        game_view=X_COSMOS()
        self.window.show_view(game_view)

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.text=""
        self.center_x=1000/2
        self.center_y=1000/2
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.text_list.append(arcade.gui.Text("Name: ",self.center_x,self.center_y))
        self.textbox_list.append(arcade.gui.TextBox(self.center_x-125,self.center_y))
        self.button_list.append(arcade.gui.SubmitButton(self.textbox_list[0],self.on_submit,self.center_x,self.center_y))
    def on_draw(self):
        arcade.start_render()
        super().on_draw()
        if self.text:
            arcade.draw_text(f"Hello {self.text}",400,100,arcade.color.GREEN,24)
        arcade.draw_text("MENU",500,500,arcade.color.WHITE,40)
        arcade.draw_text("CLICK TO PLAY",500,400,arcade.color.WHITE,40)
    def on_submit(self):
        self.text=self.textbox_list[0].text_storage.text

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
        if self.center_x==1000 and self.center_y>=300:
            self.center_y -=50
            self.center_x=0
        elif self.center_x==0 and self.center_y>=300:
            self.center_y-=50
            self.center_x==0

class LEVEL4(arcade.Sprite):
    def update(self):
        self.center_x+=BUBBLE_MOVEMENT
        self.center_y+=BUBBLE_MOVEMENT
        if self.center_x>1000:
            self.center_x=0
        if self.center_y>770:
            self.center_y=300

class LEVEL5(arcade.Sprite):
    def update(self):
        self.center_x+=5
        if self.center_x==500:
            self.center_y-=50
            self.center_x=0
class X_COSMOS(arcade.View):
    def __init__(self):
        super().__init__()
        self.score=0
        self.level=1
        self.bullet_list=self.collision_list=self.physics_engine=None
        self.player_list=self.bubble_list=None

    def level_1(self):
        self.bubble_list = arcade.SpriteList()
        for i in range(100):
            self.bubble_sprite = arcade.Sprite("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 600
            self.bubble_list.append(self.bubble_sprite)

    def level_2(self):
        for i in range(100):
            self.bubble_sprite=LEVEL2("images/Coin.png",0.40)
            self.bubble_sprite.center_x=random.randrange(50,950,30)
            self.bubble_sprite.center_y=600
            self.bubble_list.append(self.bubble_sprite)

    def level_3(self):
        for i in range(100):
            self.bubble_sprite=LEVEL3("images/Coin.png",0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 750
            self.bubble_list.append(self.bubble_sprite)

    def level_4(self):
        for i in range(100):
            self.bubble_sprite=LEVEL4("images/Coin.png",0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 750
            self.bubble_list.append(self.bubble_sprite)

    def level_5(self):
        for i in range(100):
            self.bubble_sprite = LEVEL5("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)
            self.bubble_sprite.center_y = 750
            self.bubble_list.append(self.bubble_sprite)

    def level_6(self):
        for i in range(20):
            self.bubble_sprite = LEVEL5("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(20,300,20)
            self.bubble_sprite.center_y = 500
            self.bubble_list.append(self.bubble_sprite)

    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.player_list=arcade.SpriteList()
        self.player_sprite = arcade.Sprite("images/character2.png", 1)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y =270
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
                self.score-=2


            if len(self.bubble_list)==0 and self.level==1:
                self.level+=1  # Increase the Level
                self.score=0  # Reset the score
                self.level_6()

            elif len(self.bubble_list)==0 and self.level==2:
                self.level+=1  # Increase the Level
                self.score=0 # Reset the score
                self.level_3()
            elif len(self.bubble_list)==0 and self.level==3:
                self.level+=1
                self.score=0
                self.level_4()
            elif len(self.bubble_list)==0 and self.level==4:
                self.level+=1
                self.score=0
                self.level_5()
            elif len(self.bubble_list)==0 and self.level==5:
                self.level+=1
                self.score=0
                self.level_6()


def main():
    """ Main method """
    window=arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT,GAME_TITLE)
    menu_view=MenuView()
    window.show_view(menu_view)
    arcade.run()



if __name__ == "__main__":
    main()

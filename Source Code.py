""" Imported two files arcade and random"""

import arcade
import random

""" Defining Global Variables: width, height, title of the window screen and 
 Bullet and Bubble speeds (speed with which the bubble and the bullet move)."""

WINDOW_WIDTH=1000
WINDOW_HEIGHT=1000
GAME_TITLE="X COSMOS"
BULLET_SPEED=5
BUBBLE_MOVEMENT=2

""" Views are used to move between multiple screens.
Instructions View Class is made which is accessed by the Menu View class.
Instructions on how to play the game goes here. 
Also this class is used to access the actual game class: X_Cosmos()"""

class InstructionView(arcade.View):

    """ Background color and button_sprites are created.
    Button sprite is the button which the user will click on to move to the actual game."""

    def on_show(self):
        arcade.set_background_color(arcade.color.MAROON)
        self.buttons = arcade.SpriteList()
        self.button_sprite = arcade.Sprite("images/star.png", 2)
        self.button_sprite.center_x = 700
        self.button_sprite.center_y = 300
        self.buttons.append(self.button_sprite)

    """ Instructions are written to the screen using the arcade.draw_text() function."""

    def on_draw(self):
        arcade.start_render()  # CLears the screen to the background color
        arcade.draw_text("INSTRUCTIONS",250,900,arcade.color.WHITE,40,anchor_x="center")
        arcade.draw_text("Shoot the Bubbles with the help of bullets.",10,800,arcade.color.WHITE,30)
        arcade.draw_text("The player could move by pressiong the keyboard keys.",10,700,arcade.color.WHITE,30)
        arcade.draw_text("The bullets will be fired on clicking the upper headed arrow key.",10,600,arcade.color.WHITE,30)
        arcade.draw_text("CLICK STAR TO PLAY",500,400,arcade.color.WHITE,40)
        self.buttons.draw()

    """ On clicking the mouse, the player could move to the game screen as the on_mouse_press function is called."""

    def on_mouse_press(self,x,y,button,modifiers):
        game_view=X_COSMOS()
        self.window.show_view(game_view)

class MenuView(arcade.View):
    """ The first screen that appears to the player is the MenuView screen"""

    def __init__(self):
        super().__init__()
        self.center_x=1000/2   # __init__() method used to define the center_x and center_y of the Menu_view screen
        self.center_y=1000/2

    def on_show(self):
        arcade.set_background_color(arcade.color.MAROON) # Setting Background color

    #arcade.draw_text() function is used to draw texts to the screen.

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("X COSMOS",self.center_x,self.center_y,arcade.color.WHITE,120,anchor_x="center")
        arcade.draw_text("CLICK TO PLAY",500,400,arcade.color.WHITE,40)

    """ On clicking the mouse, the player could move to the instructions screen as the on_mouse_press function is called."""

    def on_mouse_press(self,x,y,button,modifiers):
        instructions_view=InstructionView()
        self.window.show_view(instructions_view)

""" Different classes are created for different levels. Code for diiferent levels goes here."""

class LEVEL2(arcade.Sprite):                # LEVEL 2 CREATED
    def update(self):                       # THe update method updates the center_x.
        self.center_x+=BUBBLE_MOVEMENT
        if self.center_x>1000:
            self.center_x=0                 # Resets the center_x of the sprite to zero as the sprite reaches the boundary.

class LEVEL3(arcade.Sprite):                # LEVEL 3 CREATED
    def update(self):
        self.center_x += BUBBLE_MOVEMENT                    # Updates the center_x of the sprite.
        if self.center_x==1000 and self.center_y>=300:
            self.center_y -=50                              # As the sprite reaches beyond the right boundary, its center_x is reset to zero and center_y is decresed by 50 pixels
            self.center_x=0                                 # Resets the center_x of the sprite to zero as the sprite reaches the boundary.
        elif self.center_x==0 and self.center_y>=300:
            self.center_y-=50                               # # As the sprite reaches beyond the left boundary, its center_x is reset to zero and center_y is decresed by 50 pixels
            self.center_x==0                                # Resets the center_x of the sprite to zero as the sprite reaches the boundary.

class LEVEL4(arcade.Sprite):                # LEVEL 4 CREATED
    def update(self):
        self.center_x+=BUBBLE_MOVEMENT      # Updates both center_x and center_y of the sprite
        self.center_y+=BUBBLE_MOVEMENT
        if self.center_x>1000:
            self.center_x=0                 # As the sprite goes beyond the boundary, its center_x is reset to zero
        if self.center_y>770:               # If the center_y goes beyond the screen height of 770 pixels, it is reset to 300
            self.center_y=300

class LEVEL5(arcade.Sprite):               # LEVEL 5 CREATED
    def update(self):
        self.center_y+=BUBBLE_MOVEMENT     # Updates the center_y of the sprites
        if self.center_y>900:              # If the center_y exceed the screen height of 900, it resets the center_y to 400
            self.center_y=400

class LEVEL6(arcade.Sprite):                # LEVEL 6 CREATED
    def update(self):
        self.center_y-=BUBBLE_MOVEMENT      # Updates the center_y of the sprites
        if self.center_y<400:               # if center_y is less than 400, it resets the center_y to 900
            self.center_y=900


"""This is the main class of the code. All the sprites and the sprite lists are created here.
 Also the game variables are initialized here. The level classes are called here too."""

class X_COSMOS(arcade.View):
    def __init__(self):
        super().__init__()  # __init__() method used to initialize the variables and sprite lists
        self.score=0
        self.level=1
        self.time=0
        self.bullet_list=self.collision_list=self.physics_engine=None
        self.player_list=self.bubble_list=None

    """For each level class created above the bubble sprites are created here and appended to the sprite lists. """

    def level_1(self):
        self.bubble_list = arcade.SpriteList()        # Sprite Lists Created
        for i in range(100):
            self.bubble_sprite = arcade.Sprite("images/Coin.png", 0.40)     # Bubble sprite created
            self.bubble_sprite.center_x = random.randrange(50, 950, 30)     # center_x and center_y of the bubble sprite are defined. Randrange function of the random module is used.
            self.bubble_sprite.center_y = 600
            self.bubble_list.append(self.bubble_sprite)                     # Bubble sprite appended to Sprite List

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
        for i in range(25):
            self.bubble_sprite = LEVEL5("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(100, 950, 30)
            self.bubble_sprite.center_y = random.randrange(400,800,50)
            self.bubble_list.append(self.bubble_sprite)

    def level_6(self):
        for i in range(30):
            self.bubble_sprite = LEVEL5("images/Coin.png", 0.40)
            self.bubble_sprite.center_x = random.randrange(100, 950, 30)
            self.bubble_sprite.center_y = random.randrange(400,800,50)
            self.bubble_list.append(self.bubble_sprite)


    def on_show(self):

        arcade.set_background_color(arcade.color.BLACK)
        self.time=0
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
        minutes=int(self.time)//60
        seconds=int(self.time)%60
        output= f"Time: {minutes:02d}:{seconds:02d}"
        self.player_list.draw()
        self.bubble_list.draw()
        self.bullet_list.draw()
        arcade.draw_text(str("SCORE: "),700, 900, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.score),900, 900, arcade.color.WHITE, 40)
        arcade.draw_text(str("LEVEL: "), 700, 800, arcade.color.WHITE, 40)
        arcade.draw_text(str(self.level), 900, 800, arcade.color.WHITE, 40)
        arcade.draw_text(output,100,900,arcade.color.WHITE,40)

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

        self.time=self.time+delta_time

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
                #if self.time>20:
                    #self.window.show_view(GameOverView)
                self.level+=1  # Increase the Level
                self.score=0  # Reset the score
                self.time=0 # Reset the time
                self.level_5()

            elif len(self.bubble_list)==0 and self.level==2:
                self.level+=1  # Increase the Level
                self.score=0 # Reset the score
                self.time = 0  # Reset the time
                self.level_3()
            elif len(self.bubble_list)==0 and self.level==3:
                self.level+=1
                self.score=0
                self.time = 0  # Reset the time
                self.level_4()
            elif len(self.bubble_list)==0 and self.level==4:
                self.level+=1
                self.score=0
                self.time = 0  # Reset the time
                self.level_5()

            elif len(self.bubble_list)==0 and self.level==5:
                game_over_view=GameOverView()
                self.window.show_view(game_over_view)

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.center_x=1000/2
        self.center_y=1000/2
    def on_show(self):
        arcade.set_background_color(arcade.color.MAROON)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Game Over",500,500,arcade.color.WHITE,120)
        arcade.draw_text("CLICK TO RESTART ",500,300,arcade.color.WHITE,100)
    def on_mouse_press(self,x,y,button,modifiers):
        game_view=X_COSMOS()
        self.wiindow.show_view(game_view)




def main():
    """ Main method """
    window=arcade.Window(WINDOW_WIDTH,WINDOW_HEIGHT,GAME_TITLE)
    menu_view=MenuView()
    window.show_view(menu_view)
    arcade.run()



if __name__ == "__main__":
    main()
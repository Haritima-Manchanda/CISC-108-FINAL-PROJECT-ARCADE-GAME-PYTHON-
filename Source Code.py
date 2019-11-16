import arcade

""" RESOURCES
    arcade.academy
    wikipedia
    
"""
SCREEN_WIDTH=1000
SCREEN_HEIGHT=800
SCREEN_TITLE="X COSMOS"
allowed_jumps=5
spike_distance=20
class X_COSMOS(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.time=0
        self.score=0
        self.level =0
        self.lives=0
        self.player_list=None
        self.background_list=None
        self.spike_list=None
        self.physics_engine=None

    def setup(self):
        arcade.set_background_color(arcade.color.CORNFLOWER_BLUE)

        self.player_list=arcade.SpriteList()
        self.player_sprite=arcade.Sprite("images/character2.png",1.5)
        self.player_sprite.center_x=50
        self.player_sprite.center_y =270
        self.player_list.append(self.player_sprite)

        self.background_list=arcade.SpriteList()
        self.background_sprite=arcade.Sprite("images/background1.png",1)
        self.background_sprite.center_x=500
        self.background_sprite.center_y=500
        self.background_list.append(self.background_sprite)

        self.spike_list = arcade.SpriteList()
        for i in range(1,3):
            self.spike_sprite = arcade.Sprite("images/spikes.png",0.8)
            self.spike_sprite.center_x=200+5*i*spike_distance
            self.spike_sprite.center_y=270
            self.spike_list.append(self.spike_sprite)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.spike_list)

    def on_draw(self):
        arcade.start_render()

        self.background_list.draw()
        self.player_list.draw()
        self.spike_list.draw()

        arcade.draw_text(str("SCORE:"), 30, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.score), 200, 90, arcade.color.RED, 40)
        arcade.draw_text(str("LEVEL:"), 370, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.level), 530, 90, arcade.color.RED, 40)
        arcade.draw_text(str("LIVES:"), 720, 90, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.lives), 850, 90, arcade.color.RED, 40)
        arcade.draw_text(str("TIMER IN SEC: "), 610, 700, arcade.color.BLACK, 40)
        arcade.draw_text(str(self.time), 900, 700, arcade.color.RED, 40)

    def on_key_press(self,key,modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y=30
        elif key==arcade.key.DOWN:
            self.player_sprite.change_y =-30
        elif key==arcade.key.RIGHT:
            self.player_sprite.change_x=30

    def on_key_release(self,key,modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y =0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self,delta_time):
        self.physics_engine.update()
        self.time+=(round(delta_time)+1)




def main():
    window=X_COSMOS()
    window.setup()
    arcade.run()

if __name__=="__main__":
    main()




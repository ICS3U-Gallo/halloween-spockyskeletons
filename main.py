
import arcade
 
background = arcade.Sprite('background.jpg', center_x = 320, center_y = 240, scale = 1.1)
WIDTH = 640
HEIGHT = 480
 
x = 50
x_speed = 5
spider = arcade.Sprite('spider.png', center_x = x, center_y = 240, scale = 0.20)
window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
 
 
 
def setup():
   arcade.schedule(update, 1/60)
   arcade.run()
 
 
def update (delta_time):
   global x, x_speed
   spider.update()
  
 
  
 
@window.event
def on_draw():
   arcade.start_render()
   # Draw in here...
   background.draw()
   spider.draw()
   if spider.center_x <= WIDTH - 50:
       spider.center_x += x_speed
  
 
@window.event
def on_key_press(key, modifiers):
   pass
 
 
@window.event
def on_key_release(key, modifiers):
   pass
 
 
@window.event
def on_mouse_press(x, y, button, modifiers):
   pass
 
 
if __name__ == '__main__':
   setup()

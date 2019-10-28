import arcade

background = arcade.Sprite('background.jpg', center_x = 320, center_y = 240, scale = 1.1)
WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
x = 50
x_speed = 1


def setup():
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass

@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(x, 100, 25, arcade.color.BLUE)
    background.draw()


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

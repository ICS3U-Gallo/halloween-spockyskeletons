import arcade

WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")


def setup():
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1 / 60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...

    arcade.draw_rectangle_filled(320, 50, 640, 100, arcade.color.GREEN)
    arcade.draw_circle_filled(WIDTH - 100, HEIGHT - 100, 50, arcade.color.YELLOW)


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

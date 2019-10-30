import arcade
import random

background = arcade.Sprite('background.jpg', center_x=320, center_y=240, scale=1.1)
WIDTH = 640
HEIGHT = 480

x = 50
x_speed = 25
y = 240
y_speed = 25
spider = arcade.Sprite('spider.png', center_x=x, center_y=y, scale=0.15)
window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
score = 0

def setup():
    arcade.schedule(update, 1 / 60)
    arcade.run()


def update(delta_time):
    global x, x_speed, spider, y, y_speed
    spider.update()

    if spider.center_x <= 15:
        x_speed = random.randint(15, 50)

    elif spider.center_x >= (WIDTH-15):
        x_speed = random.randint(-50, -10)
    spider.center_x += x_speed

    if spider.center_y <= 15:
        y_speed = random.randint(15, 50)
    elif spider.center_y >= (HEIGHT - 15):
        y_speed = random.randint(-50, -10)
    spider.center_y += y_speed



@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    background.draw()
    spider.draw()
    arcade.draw_text(f"Score {score}", WIDTH - 80, HEIGHT - 40, arcade.color.WHITE, 14)


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()

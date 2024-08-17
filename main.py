# %%
from pyglet import app
from pyglet.window import Window, key
from pyglet.text import Label
from pyglet.resource import image
from pyglet.clock import schedule_interval

# from dummie import Dummie
from hero import Hero


# %%
WINDOW = Window()  # fullscreen=True

# animation = load_animation("resources/char/running_hero.gif")
# bin = TextureBin()
# animation.add_to_texture_bin(bin)
# sprite = Sprite(img=animation)

# animation = animation("resources/char/running_hero.gif")


HERO = Hero(
    # resource=animation,
    x=WINDOW.width // 2,
    y=10,
)
FONT_SIZE = 24
BACKGROUND = image("resources/background.jpg")
GREET_LBL = Label(
    text="Вітаю на прокачку)",
    font_name="Roboto",
    font_size=FONT_SIZE,
    bold=True,
    x=WINDOW.width // 2,
    y=WINDOW.height - FONT_SIZE // 2,  # // 2 - FONT_SIZE,
    anchor_x="center",
    anchor_y="center",
)
schedule_interval(HERO.update, 1 / 60.0)

# %%


@WINDOW.event
def on_draw():
    WINDOW.clear()
    BACKGROUND.blit(0, 0, width=WINDOW.width - 1, height=WINDOW.height - 1)
    HERO.draw()
    GREET_LBL.draw()


# %%
from direction import Direction


@WINDOW.event
def on_key_press(symbol, modifiers):
    match symbol:
        case key.A:
            print("Left direction")
            HERO.move(direction=Direction.LEFT)
        case key.D:
            print("Right direction")
            HERO.move(direction=Direction.RIGHT)

        case key.SPACE:
            print("Jump")
            HERO.jump()
        case key.MOD_CTRL:
            print("CROWD")
            HERO.move(direction=Direction.CROWD)

        case key.ESCAPE:
            print("Quit the game)")
            app.exit()

        case _:
            return
    # print(f'{symbol=} {modifiers=}')


# %%
app.run()
